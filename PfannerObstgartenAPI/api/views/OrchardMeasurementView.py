from django.shortcuts import get_object_or_404
from api.serializers import OrchardMeasurementSerializer, WriteOrchardMeasurementSerializer, TreeSerializer
from api.models import OrchardMeasurement, Tree
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status

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

    def get_queryset(self):
        queryset = OrchardMeasurement.objects.all()
        frostSensitivity = self.request.query_params.get('frostSensitivity')
        growthHabit = self.request.query_params.get('growthHabit')
        yieldHabit = self.request.query_params.get('yieldHabit')
        precipitation = self.request.query_params.get('precipitation')
        temperature = self.request.query_params.get('temperature')
        season = self.request.query_params.get('season')
        lateFrost = self.request.query_params.get('lateFrost')
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

        if season is not None:
            filtersApplied = True
            queryset = queryset.filter(season=season)

        if lateFrost is not None:
            filtersApplied = True
            queryset = queryset.filter(lateFrost=lateFrost)

        if filtersApplied:
            filteredIds.append(queryset.values_list('tree_id', flat=True))
            queryset = Tree.objects.all()
            queryset = queryset.filter(pk__in=filteredIds)
        else:
            queryset = Tree.objects.all()

        return queryset
