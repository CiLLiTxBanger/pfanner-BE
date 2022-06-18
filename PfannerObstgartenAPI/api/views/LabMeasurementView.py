from api.serializers import LabMeasurementSerializer, WriteLabMeasurementSerializer, TreeSerializer
from api.models import LabMeasurement, Tree
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

class LabMeasurementListByTreeId(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(request, self, treeId, format=None):
        labMeasurements = LabMeasurement.objects.filter(tree = treeId)
        serializer = LabMeasurementSerializer(labMeasurements, many = True)
        permission_classes = [permissions.IsAuthenticated]
        #permission_classes = [admin]
        return Response(serializer.data)

    def post(request, self, treeId):
        labMeasurement = self.data
        #Create LabMeasurement from above data
        serializer = LabMeasurementSerializer(data=labMeasurement)
        permission_classes = [permissions.IsAuthenticated]
        if serializer.is_valid(raise_exception=True):
            labMeasurement_saved = serializer.save()
        return Response({"success": "Success!"})
        
class LabMeasurementList(generics.ListCreateAPIView):
    queryset = LabMeasurement.objects.all()
    serializer_class = LabMeasurementSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return WriteLabMeasurementSerializer
        return LabMeasurementSerializer

class LabMeasurementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LabMeasurement.objects.all()
    serializer_class = LabMeasurementSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return WriteLabMeasurementSerializer
        return LabMeasurementSerializer

class TreesFilteredByLabMeasurementStats(generics.ListAPIView):
    queryset = LabMeasurement.objects.all()
    serializer_class = TreeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = LabMeasurement.objects.all()
        acidity_from = self.request.query_params.get('acidity_from')
        acidity_to = self.request.query_params.get('acidity_to')
        flavor = self.request.query_params.get('flavor')
        strength_from = self.request.query_params.get('strength_from')
        strength_to = self.request.query_params.get('strength_to')
        sugar_from = self.request.query_params.get('sugar_from')
        sugar_to = self.request.query_params.get('sugar_to')
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

        if filtersApplied:
            filteredIds.append(queryset.values_list('tree_id', flat=True))
            queryset = Tree.objects.all()
            queryset = queryset.filter(pk__in=filteredIds)
        else:
            queryset = Tree.objects.all()

        return queryset