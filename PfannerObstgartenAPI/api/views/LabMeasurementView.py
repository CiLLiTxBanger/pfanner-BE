from api.serializers import LabMeasurementSerializer
from api.models import LabMeasurement
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

class LabMeasurementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LabMeasurement.objects.all()
    serializer_class = LabMeasurementSerializer
    permission_classes = [permissions.IsAuthenticated]