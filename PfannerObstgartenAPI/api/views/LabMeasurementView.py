from api.serializers import LabMeasurementSerializer, WriteLabMeasurementSerializer, TreeSerializer
from api.models import LabMeasurement, Tree
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import filters

class LabMeasurementListByTreeId(APIView):
    """
    Get a List of all LabMeasurements by TreeId. Authentication required
    """
    permission_classes = [permissions.IsAuthenticated]
    def get(request, self, treeId, format=None):
        labMeasurements = LabMeasurement.objects.filter(tree = treeId)
        serializer = LabMeasurementSerializer(labMeasurements, many = True)
        return Response(serializer.data)
        
class LabMeasurementList(generics.ListCreateAPIView):
    """
    Get a List of all LabMeasurements or create a LabMeasurement. Authentication required
    """
    queryset = LabMeasurement.objects.all()
    serializer_class = LabMeasurementSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return WriteLabMeasurementSerializer
        return LabMeasurementSerializer

class LabMeasurementDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or Update a LabMeasurement. Authentication required
    """
    queryset = LabMeasurement.objects.all()
    serializer_class = LabMeasurementSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return WriteLabMeasurementSerializer
        return LabMeasurementSerializer

class TreesFilteredByLabMeasurementStats(generics.ListAPIView):
    """
    Get a List of Trees filtered by Labmeasurementstats. Authentication required
    """
    queryset = LabMeasurement.objects.all()
    serializer_class = TreeSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['type', 'variety__name', 'variety__blossom', 'variety__climate', 'variety__pick_maturity',
     'variety__usage', 'variety__pollinator', 'variety__properties', 'variety__output', 'variety__disease_possibility', 'variety__description']

    def get_queryset(self):
        queryset = LabMeasurement.objects.all()
        acidity_from = self.request.query_params.get('acidity_from')
        acidity_to = self.request.query_params.get('acidity_to')
        flavor = self.request.query_params.get('flavor')
        strength_from = self.request.query_params.get('strength_from')
        strength_to = self.request.query_params.get('strength_to')
        sugar_from = self.request.query_params.get('sugar_from')
        sugar_to = self.request.query_params.get('sugar_to')
        row = self.request.query_params.get('row')
        column = self.request.query_params.get('column')
        treeid = self.request.query_params.get('treeid')
        location = self.request.query_params.get('location')
        filteredIds = []
        filtersApplied = False

        if acidity_from is not None:
            filtersApplied = True
            queryset = queryset.filter(acidMeasurement__gte=acidity_from)

        if acidity_to is not None:
            filtersApplied = True
            queryset = queryset.filter(acidMeasurement__lte=acidity_to)

        if strength_from is not None:
            filtersApplied = True
            queryset = queryset.filter(strengthMeasurement__gte=strength_from)

        if strength_to is not None:
            filtersApplied = True
            queryset = queryset.filter(strengthMeasurement__lte=strength_to)

        if sugar_from is not None:
            filtersApplied = True
            queryset = queryset.filter(sugarMeasurement__gte=sugar_from)

        if sugar_to is not None:
            filtersApplied = True
            queryset = queryset.filter(sugarMeasurement__lte=sugar_to)

        if flavor is not None:
            filtersApplied = True
            queryset = queryset.filter(flavorMeasurement=flavor)

        if row is not None:
            filtersApplied = True
            queryset = queryset.filter(tree__row=row)

        if column is not None:
            filtersApplied = True
            queryset = queryset.filter(tree__column=column)

        if treeid is not None:
            filtersApplied = True
            queryset = queryset.filter(tree__id=treeid)

        if filtersApplied:
            filteredIds.append(queryset.values_list('tree_id', flat=True))
            queryset = Tree.objects.all()
            queryset = queryset.filter(pk__in=filteredIds)
        else:
            queryset = Tree.objects.all()

        if location is not None:
            queryset = queryset.filter(location=location)
        return queryset