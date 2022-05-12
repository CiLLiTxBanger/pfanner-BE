from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import UserSerializer
from api.models import Tree
from api.serializers import TreeSerializer
from django.core.exceptions import ValidationError

class TestPostView(APIView):
    """
    A view that can accept POST requests with JSON content.
    """
    parser_classes = [JSONParser]

    def post(self, request, format=None):
        return Response(request.data)

    