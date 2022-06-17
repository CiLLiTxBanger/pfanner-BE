from api.models import Tree
from api.serializers import TreeSerializer, WriteTreeSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from rest_framework import filters


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