import re
from webbrowser import get
from rest_framework import permissions
from api.models import Variety, Tree
from api.serializers import VarietySerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework import filters


class VarietyList(generics.ListCreateAPIView):
    """
    List all Varieties, or create a new Variety. Im moment noch alles ohne Authentification möglich.
    """
    queryset = Variety.objects.all()
    serializer_class = VarietySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'blossom', 'fruit', 'climate', 'pick_maturity', 'usage', 'pollinator', 'properties', 'output', 'disease_possibility', 'description']

    def get_queryset(self):
        queryset = Tree.objects.all()
        location = self.request.query_params.get('location')
        filteredIds = []
        filtersApplied = False

        if location is not None:
            filtersApplied = True
            queryset = queryset.filter(location=location)

        if filtersApplied:
            filteredIds.append(queryset.values_list('variety_id', flat=True))
            queryset = Variety.objects.all()
            queryset = queryset.filter(pk__in=filteredIds)
        else:
            queryset = Variety.objects.all()
        return queryset


class VarietyDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a Variety. Im moment noch alles ohne Authentification möglich.
    """
    queryset = Variety.objects.all()
    serializer_class = VarietySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class VarietyByTreeId(APIView):
    """
    Retrieve a variety instance by tree id in url.
    """
    def get_object(self, pk):
        try:
            return Variety.objects.get(pk=pk)
        except Variety.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        variety = self.get_object(pk)
        serializer = VarietySerializer(variety)
        #serializer.data['image_photo'] = request.get_host() + serializer.data['image_photo']
        return Response(serializer.data)