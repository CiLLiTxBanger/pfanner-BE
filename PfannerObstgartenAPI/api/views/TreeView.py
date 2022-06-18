from gc import get_objects
from api.models import Tree, OrchardMeasurement, LabMeasurement
from api.serializers import TreeSerializer, WriteTreeSerializer, WriteOrchardMeasurementSerializer, WriteLabMeasurementSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from rest_framework import filters
from rest_framework.views import APIView
from datetime import datetime
from rest_framework import status


class TreeList(generics.ListCreateAPIView):
    """
    List all Trees, or create a new Tree.
    """
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['type', 'variety__name', 'variety__blossom', 'variety__fruit', 'variety__climate', 'variety__pick_maturity',
     'variety__usage', 'variety__pollinator', 'variety__properties', 'variety__output', 'variety__disease_possibility', 'variety__description']

    def perform_create(self, serializer):
        queryset = Tree.objects.filter(column=self.request.data['column'], row=self.request.data['row'], location=self.request.data['location'], active = 1)
        if queryset.exists():
            raise ValidationError('Position is already in use')
        serializer.save()
        
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return WriteTreeSerializer
        return TreeSerializer

class TreeDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a Tree.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer

    def get_serializer_class(self):
        if self.request.method == 'PATCH' or self.request.method == 'PUT':
            return WriteTreeSerializer
        return TreeSerializer

class TreeAnalytics(APIView):
    """
    Retrieve a variety instance by tree id in url.
    """

    def get(self, request, pk, format=None):
        orchardmeasurements = OrchardMeasurement.objects.filter(tree__id=pk)
        labmeasurements = LabMeasurement.objects.filter(tree__id=pk)

        if not orchardmeasurements and not labmeasurements:
            return Response(data={"message": "There is no Tree with the given id"}, status=status.HTTP_204_NO_CONTENT)

        year_from = self.request.query_params.get('year_from')
        year_to = self.request.query_params.get('year_to')

        if year_from is not None:
            day_year_from = datetime(int(year_from), 1, 1)
            orchardmeasurements = orchardmeasurements.filter(created_on__year__gte=day_year_from.year, status=1)
            labmeasurements = labmeasurements.filter(timestamp__year__gte=day_year_from.year, status=1)

        if year_to is not None:
            day_year_to = datetime(int(year_to), 1, 1)
            orchardmeasurements = orchardmeasurements.filter(created_on__year__lte=day_year_to.year, status=1)
            labmeasurements = labmeasurements.filter(timestamp__year__lte=day_year_to.year, status=1)


        orchardSerializer = WriteOrchardMeasurementSerializer(orchardmeasurements, many=True)
        labSerializer = WriteLabMeasurementSerializer(labmeasurements, many=True)
        data = {'OrchardMeasurements': orchardSerializer.data, 'LabMeasurements': labSerializer.data}

        
        return Response(data=data, status=status.HTTP_200_OK)