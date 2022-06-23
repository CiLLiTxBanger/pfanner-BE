from django.shortcuts import get_object_or_404
from api.serializers import OrchardMeasurementSerializer, WriteOrchardMeasurementSerializer, TreeSerializer
from api.models import OrchardMeasurement, Tree
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework import filters

class OrchardMeasurementListByTreeId(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(request, self, treeId, format=None):
        orchardMeasurements = OrchardMeasurement.objects.filter(tree = treeId)
        serializer = OrchardMeasurementSerializer(orchardMeasurements, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class OrchardMeasurementList(generics.ListCreateAPIView):
    queryset = OrchardMeasurement.objects.all()
    serializer_class = OrchardMeasurementSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return WriteOrchardMeasurementSerializer
        return OrchardMeasurementSerializer

class OrchardMeasurementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrchardMeasurement.objects.all()
    serializer_class = OrchardMeasurementSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return WriteOrchardMeasurementSerializer
        return OrchardMeasurementSerializer

class TreesFilteredByOrchardMeasurementStats(generics.ListAPIView):
    queryset = OrchardMeasurement.objects.all()
    serializer_class = TreeSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['type', 'variety__name', 'variety__blossom', 'variety__fruit', 'variety__climate', 'variety__pick_maturity',
     'variety__usage', 'variety__pollinator', 'variety__properties', 'variety__output', 'variety__disease_possibility', 'variety__description']

    def get_queryset(self):
        queryset = OrchardMeasurement.objects.all()
        frostSensitivity = self.request.query_params.get('frostSensitivity')
        growthHabit = self.request.query_params.get('growthHabit')
        yieldHabit = self.request.query_params.get('yieldHabit')
        precipitation = self.request.query_params.get('precipitation')
        temperature = self.request.query_params.get('temperature')
        row = self.request.query_params.get('row')
        column = self.request.query_params.get('column')
        treeid = self.request.query_params.get('treeid')
        lateFrost = self.request.query_params.get('lateFrost')
        location = self.request.query_params.get('location')
        filteredIds = []
        filtersApplied = False

        if frostSensitivity is not None:
            filtersApplied = True
            queryset = queryset.filter(frostSensitivity=frostSensitivity)

        if growthHabit is not None:
            filtersApplied = True
            queryset = queryset.filter(growthHabit=growthHabit)

        if yieldHabit is not None:
            filtersApplied = True
            queryset = queryset.filter(yieldHabit=yieldHabit)

        if precipitation is not None:
            filtersApplied = True
            queryset = queryset.filter(precipitation=precipitation)

        if temperature is not None:
            filtersApplied = True
            queryset = queryset.filter(temperature=temperature)

        if row is not None:
            filtersApplied = True
            queryset = queryset.filter(tree__row=row)

        if column is not None:
            filtersApplied = True
            queryset = queryset.filter(tree__column=column)

        if treeid is not None:
            filtersApplied = True
            queryset = queryset.filter(tree__id=treeid)

        if lateFrost is not None:
            filtersApplied = True
            queryset = queryset.filter(lateFrost=lateFrost)

        if filtersApplied:
            filteredIds.append(queryset.values_list('tree_id', flat=True))
            queryset = Tree.objects.all()
            queryset = queryset.filter(pk__in=filteredIds)
        else:
            queryset = Tree.objects.all()

        if location is not None:
            queryset = queryset.filter(location=location)
        return queryset
