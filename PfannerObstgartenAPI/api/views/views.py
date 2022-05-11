# under construction

from django.contrib.auth.models import User
from rest_framework import permissions
from api.serializers import UserSerializer
from api.models import Tree
from api.serializers import TreeSerializer
from rest_framework import generics
from rest_framework import permissions
#from api.permissions import IsOwnerOrReadOnly         #wird für die authentifizierung benötigt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'trees': reverse('tree-list', request=request, format=format)
    })

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TreeList(generics.ListCreateAPIView):
    """
    List all Trees, or create a new Tree.
    """
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TreeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a Tree.
    """
   # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer

