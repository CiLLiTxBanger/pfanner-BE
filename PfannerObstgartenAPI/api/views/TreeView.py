from api.models import Tree
from api.serializers import TreeSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.exceptions import ValidationError


class TreeList(generics.ListCreateAPIView):
    """
    List all Trees, or create a new Tree.
    """
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        queryset = Tree.objects.filter(column=self.request.data['column'], row=self.request.data['row'], location=self.request.data['location'], active = 1)
        if queryset.exists():
            raise ValidationError('Position is already in use')
        serializer.save()
        #serializer.save(owner=self.request.user)

class TreeDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve, update or delete a Tree.
    """
   # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer