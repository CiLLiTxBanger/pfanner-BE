from api.serializers import DiseaseSerializer
from api.serializers import DiseaseMeasurementSerializer, WriteDiseaseMeasurementSerializer

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

class DiseaseDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve or update a Disease.
    """
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DiseaseMeasurementByOrchardMeasurementList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(request, self, orchardMeasurementId, format=None):
            diseaseMeasurements = DiseaseMeasurement.objects.filter(orchardMeasurement = orchardMeasurementId)
            serializer = DiseaseMeasurementSerializer(diseaseMeasurements, many = True)
            return Response(serializer.data)

class DiseaseMeasurementList(generics.ListCreateAPIView):
    queryset = DiseaseMeasurement.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return WriteDiseaseMeasurementSerializer
        return DiseaseMeasurementSerializer

    def get_serializer(self, *args, **kwargs):
        """ if an array is passed, set serializer to many """
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(DiseaseMeasurementList, self).get_serializer(*args, **kwargs)

class DiseaseMeasurementDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve or update a Disease.
    """
    queryset = DiseaseMeasurement.objects.all()
    serializer_class = DiseaseMeasurementSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]