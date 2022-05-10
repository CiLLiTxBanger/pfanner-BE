from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('', views.api_root),
    path('api/trees/', views.TreeList.as_view(), name='tree-list'),
    path('api/trees/<int:pk>/', views.TreeDetail.as_view(), name='tree-detail'),
    #path('users/', views.UserList.as_view(), name='user-list'),
    #path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)