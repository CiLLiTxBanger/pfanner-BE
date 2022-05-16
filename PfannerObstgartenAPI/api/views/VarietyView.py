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
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view


class VarietyList(generics.ListCreateAPIView):
    """
    List all Varieties, or create a new Variety. Im moment noch alles ohne Authentification möglich.
    """
    queryset = Variety.objects.all()
    serializer_class = VarietySerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class VarietyDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve, update or delete a Variety. Im moment noch alles ohne Authentification möglich.
    """
    queryset = Variety.objects.all()
    serializer_class = VarietySerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class VarietyByTreeId(APIView):
    """
    Retrieve a variety instance by tree id in url.
    """
    def get_object(self, pk):
        try:
            return Variety.objects.get(pk=pk)
        except Variety.DoesNotExist:
            raise Http404

    def get_TreeId(self, pk):
        try:
            return Tree.objects.filter(pk=pk).values_list('id')
        except Tree.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        treeid = self.get_TreeId(pk)
        variety = self.get_object(treeid[0][0])
        serializer = VarietySerializer(variety)
        return Response(serializer.data)

class VarietyImageTest(generics.RetrieveUpdateAPIView):
    queryset = Image.objects.order_by('created_on')
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser, FormParser)
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        all_images = Image.objects.all()
        serializer = ImageSerializer(all_images, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                photo=request.data.get('photo')
            )
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)