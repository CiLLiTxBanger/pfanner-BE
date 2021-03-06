# under construction

from django.contrib.auth.models import User
from rest_framework import permissions
from api.serializers import UserSerializer
from rest_framework import generics
from rest_framework import permissions
#from api.permissions import IsOwnerOrReadOnly         #wird für die authentifizierung benötigt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'trees': reverse('tree-list', request=request, format=format),
        'varieties': reverse('variety-list', request=request, format=format),
        'locations': reverse('location-list', request=request, format=format),
        'labmeasurements': reverse('labmeasurement-list', request=request, format=format),
        'orchardmeasurements': reverse('orchardmeasurement-list', request=request, format=format),
        'diseases': reverse('disease-list', request=request, format=format),
        'diseasemeasurements': reverse('diseasemeasurement-list', request=request, format=format),
    })

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]



