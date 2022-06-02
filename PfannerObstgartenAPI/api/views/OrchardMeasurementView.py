from api.serializers import OrchardMeasurementSerializer
from api.models import OrchardMeasurement
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

class OrchardMeasurementList(APIView):
    #serializer_class = OrchardMeasurementSerializer
    def get(request, self, treeId, format=None):
        orchardMeasurements = OrchardMeasurement.objects.filter(tree = treeId)
        serializer = OrchardMeasurementSerializer(orchardMeasurements, many = True)
        #permission_classes = [admin]
        return Response(serializer.data)



class OrchardMeasurementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrchardMeasurement.objects.all()
    serializer_class = OrchardMeasurementSerializer
    #permission_classes = [admin]