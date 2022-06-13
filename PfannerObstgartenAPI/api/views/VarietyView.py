from rest_framework import permissions
from api.models import Variety
from api.serializers import VarietySerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework.decorators import api_view


class VarietyList(generics.ListCreateAPIView):
    """
    List all Varieties, or create a new Variety. Im moment noch alles ohne Authentification möglich.
    """
    queryset = Variety.objects.all()
    serializer_class = VarietySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class VarietyDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a Variety. Im moment noch alles ohne Authentification möglich.
    """
    queryset = Variety.objects.all()
    serializer_class = VarietySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_destroy(self, instance):
        variety = self.get_object()
        variety.image.delete()
        return super().perform_destroy(instance) 

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
        serializer.data['image']['photo'] = request.get_host() + serializer.data['image']['photo']
        return Response(serializer.data)