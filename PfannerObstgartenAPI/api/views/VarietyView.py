from rest_framework import permissions
from api.models import Variety
from api.serializers import VarietySerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class VarietyList(generics.ListCreateAPIView):
    """
    List all Trees, or create a new Tree.
    """
    queryset = Variety.objects.all()
    serializer_class = VarietySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class VarietyDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve, update or delete a Tree.
    """
    queryset = Variety.objects.all()
    serializer_class = VarietySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class VarietyByTreeId(APIView):
    """
    Retrieve a variety instance.
    """
    def get_object(self, pk):
        try:
            return Variety.objects.get(pk=pk)
        except Variety.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        variety = self.get_object(pk)
        serializer = VarietySerializer(variety)
        return Response(serializer.data)