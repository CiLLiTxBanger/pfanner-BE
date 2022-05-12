from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('', views.api_root),
     path('api/varieties/', views.VarietyView.VarietyList.as_view(), name='variety-list'),
     path('api/varieties/<int:pk>/', views.VarietyDetail.as_view(), name='variety-detail'),
     path('api/getvarietybytreeid/<int:pk>/', views.VarietyByTreeId.as_view(), name='varietyByTreeId'),
     path('api/trees/', views.views.TreeList.as_view(), name='tree-list'),
     path('api/trees/<int:pk>/', views.views.TreeDetail.as_view(), name='tree-detail'),
     path('users/', views.views.UserList.as_view(), name='user-list'),
     path('users/<int:pk>/', views.views.UserDetail.as_view(), name='user-detail'),
     path('testpostview/', views.testPostView.TestPostView.as_view(), name='testexampleview'),
#    path('test', views.test.current_datetime)
]

urlpatterns = format_suffix_patterns(urlpatterns)