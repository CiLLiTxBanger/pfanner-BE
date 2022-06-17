from django.shortcuts import get_object_or_404
from api.serializers import OrchardMeasurementSerializer, WriteOrchardMeasurementSerializer
from api.models import OrchardMeasurement
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
        if self.request.method == 'PUT':
            return WriteOrchardMeasurementSerializer
        return OrchardMeasurementSerializer
