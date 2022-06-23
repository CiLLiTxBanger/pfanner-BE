from gc import get_objects
import http
from http.client import NETWORK_AUTHENTICATION_REQUIRED
from os import stat
from telnetlib import STATUS
from api.models import Tree, OrchardMeasurement, LabMeasurement
from api.serializers import TreeSerializer, WriteTreeSerializer, WriteOrchardMeasurementSerializer, WriteLabMeasurementSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.views import APIView
from datetime import datetime
from rest_framework import status
from django.http import *
from rest_framework.exceptions import APIException
from django.db.models import Q


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
            raise NotAllParametersAvailable()
        else:
            serializer.save()
        
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return WriteTreeSerializer
        return TreeSerializer

    def get_queryset(self):
        queryset = Tree.objects.all()
        location = self.request.query_params.get('location')

        if location is not None:
            queryset = queryset.filter(location=location)
            return queryset
        return queryset

class NotAllParametersAvailable(APIException):
    status_code = 418
    default_detail = 'Not all required parameters passed. The following parameters have to be passed: row, column and location.'
    default_code = 'i_am_a_Teapot'

class PositionAlreadyInUse(APIException):
    status_code = 418
    default_detail = 'There is already a active tree on this position'
    default_code = 'i_am_a_Teapot'

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

    def perform_update(self, serializer):
        if "active" in self.request.data:
            if self.request.data['active'] == 0:
                return super().perform_update(serializer)
        if 'column' in self.request.data and 'row' in self.request.data and 'location' in self.request.data:
            column = self.request.data['column']
            row = self.request.data['row']
            location = self.request.data['location']
            if column is not None and row is not None and location is not None:
                queryset = Tree.objects.filter(column=column, row=row, location=location, active = 1)
                if queryset.exists():
                    queryset = queryset.filter(pk=self.kwargs['pk'])
                    if queryset.exists():
                        return super().perform_update(serializer)                       
                    raise PositionAlreadyInUse()
                return super().perform_update(serializer)
        raise NotAllParametersAvailable()

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
        month_from = self.request.query_params.get('month_from')
        month_to = self.request.query_params.get('month_to')

        if year_from is not None:
            day_year_from = datetime(int(year_from), 1, 1)
            orchardmeasurements = orchardmeasurements.filter(created_on__year__gte=day_year_from.year, status=1)
            labmeasurements = labmeasurements.filter(timestamp__year__gte=day_year_from.year, status=1)
        
        if month_from is not None and year_from is not None:
            date = datetime(int(year_from), int(month_from), 1)
            orchardmeasurements = orchardmeasurements.filter(Q(created_on__year=date.year, created_on__month__gte=date.month) | Q(created_on__year__gt=date.year), status=1)
            labmeasurements = labmeasurements.filter(Q(timestamp__year=date.year, timestamp__month__gte=date.month) | Q(timestamp__year__gt=date.year), status=1)

        if year_to is not None:
            day_year_to = datetime(int(year_to), 1, 1)
            orchardmeasurements = orchardmeasurements.filter(created_on__year__lte=day_year_to.year, status=1)
            labmeasurements = labmeasurements.filter(timestamp__year__lte=day_year_to.year, status=1)
        
        if month_to is not None and year_to is not None:
            date = datetime(int(year_to), int(month_to), 1)
            orchardmeasurements = orchardmeasurements.filter(Q(created_on__year=date.year, created_on__month__lte=date.month) | Q(created_on__year__lt=date.year), status=1)
            labmeasurements = labmeasurements.filter(Q(timestamp__year=date.year, timestamp__month__gte=date.month) | Q(timestamp__year__gt=date.year), status=1)


        orchardSerializer = WriteOrchardMeasurementSerializer(orchardmeasurements, many=True)
        labSerializer = WriteLabMeasurementSerializer(labmeasurements, many=True)
        data = {'OrchardMeasurements': orchardSerializer.data, 'LabMeasurements': labSerializer.data}

        
        return Response(data=data, status=status.HTTP_200_OK)