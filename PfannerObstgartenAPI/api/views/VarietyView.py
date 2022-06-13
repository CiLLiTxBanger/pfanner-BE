from rest_framework import permissions
from api.models import Variety
from api.models import Image
from api.serializers import VarietySerializer
from api.models import Tree
from api.serializers import TreeSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from api.serializers import ImageSerializer
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.decorators import api_view


class VarietyList(generics.ListCreateAPIView):
    """
    List all Varieties, or create a new Variety. Im moment noch alles ohne Authentification möglich.
    """
    queryset = Variety.objects.all()
    serializer_class = VarietySerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class VarietyDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a Variety. Im moment noch alles ohne Authentification möglich.
    """
    queryset = Variety.objects.all()
    serializer_class = VarietySerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

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

class ImageList(generics.ListCreateAPIView):
    """
    List all images, or create an image. Im moment noch alles ohne Authentification möglich.
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve or update an image. Im moment noch alles ohne Authentification möglich.
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class VarietyImageTest(generics.ListCreateAPIView):
    queryset = Variety.objects.order_by('created_on')
    serializer_class = VarietySerializer
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        all_varieties = Variety.objects.all()
        serializer = VarietySerializer(all_varieties, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VarietySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)