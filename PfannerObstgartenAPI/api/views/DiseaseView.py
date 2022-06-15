from api.serializers import DiseaseSerializer
from api.serializers import DiseaseMeasurementSerializer

from api.models import Disease
from api.models import DiseaseMeasurement

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions

class DiseaseList(generics.CreateAPIView, generics.ListAPIView):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer
    permission_classes = [permissions.IsAuthenticated]


class DiseaseMeasurementByOrchardMeasurementList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(request, self, orchardMeasurementId, format=None):
            diseaseMeasurements = DiseaseMeasurement.objects.filter(orchardMeasurement = orchardMeasurementId)
            serializer = DiseaseMeasurementSerializer(diseaseMeasurements, many = True)
            return Response(serializer.data)

class DiseaseMeasurementList(generics.ListCreateAPIView):
    queryset = DiseaseMeasurement.objects.all()
    serializer_class = DiseaseMeasurementSerializer
    permission_classes = [permissions.IsAuthenticated]