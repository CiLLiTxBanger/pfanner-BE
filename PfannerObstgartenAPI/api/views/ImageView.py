from rest_framework import permissions
from api.models import Image
from rest_framework import generics
from rest_framework import permissions
from api.serializers import ImageSerializer
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.decorators import api_view

class ImageList(generics.ListCreateAPIView):
    """
    List all images, or create an image. Im moment noch alles ohne Authentification möglich.
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]

class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve or update an image. Im moment noch alles ohne Authentification möglich.
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

