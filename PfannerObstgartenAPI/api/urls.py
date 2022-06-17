from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.api_root),
     path('api/varieties/', views.VarietyView.VarietyList.as_view(), name='variety-list'),
     path('api/varieties/<int:pk>/', views.VarietyDetail.as_view(), name='variety-detail'),
     path('api/getvarietybytreeid/<int:pk>/', views.VarietyByTreeId.as_view(), name='varietyByTreeId'),
     path('api/images/', views.ImageView.ImageList.as_view(), name='image-list'),
     path('api/images/<int:pk>/', views.ImageView.ImageDetail.as_view(), name='image-detail'),
     path('api/trees/', views.TreeList.as_view(), name='tree-list'),
     path('api/trees/<int:pk>/', views.TreeDetail.as_view(), name='tree-detail'),
     path('api/locations/', views.LocationView.LocationList.as_view(), name='location-list'),
     path('api/locations/<int:pk>/', views.LocationView.LocationDetail.as_view(), name='location-detail'),
     path('users/', views.views.UserList.as_view(), name='user-list'),
     path('users/<int:pk>/', views.views.UserDetail.as_view(), name='user-detail'),
     path('api/trees/<int:treeId>/orchardmeasurements/', views.OrchardMeasurementView.OrchardMeasurementListByTreeId.as_view(), name='orchardmeasurementbytreeid-list'),
     path('api/orchardmeasurements/', views.OrchardMeasurementView.OrchardMeasurementList.as_view(), name='orchardmeasurement-list'),
     path('api/orchardmeasurements/<int:pk>/', views.OrchardMeasurementView.OrchardMeasurementDetail.as_view(), name='orchardmeasurement-detail'),
     path('api/trees/<int:treeId>/labmeasurements/', views.LabMeasurementView.LabMeasurementListByTreeId.as_view(), name='labmeasurementbytreeid-list'),
     path('api/labmeasurements/<int:pk>/', views.LabMeasurementView.LabMeasurementDetail.as_view(), name='labmeasurement-detail'),
     path('api/labmeasurements/', views.LabMeasurementView.LabMeasurementList.as_view(), name='labmeasurement-list'),
     path('api/diseases/', views.DiseaseView.DiseaseList.as_view(), name='disease-list'),
     path('api/diseases/<int:pk>', views.DiseaseView.DiseaseDetail.as_view(), name='disease-detail'),
     path('api/diseasemeasurements/', views.DiseaseView.DiseaseMeasurementList.as_view(), name='diseasemeasurement-list'),
     path('api/orchardmeasurements/<int:orchardMeasurementId>/diseasemeasurements', views.DiseaseView.DiseaseMeasurementByOrchardMeasurementList.as_view(), name='diseasemeasurementbyorchardmeasurement-list'),
     path('api/trees/<int:treeId>/labmeasurements/csv', views.CsvView.ExportLabMeasurementsCSVByTreeId.as_view(), name='labmeasurement-csv'),
     path('api/trees/<int:treeId>/orchardmeasurements/csv', views.CsvView.ExportOrchardMeasurementsCSVByTreeId.as_view(), name='orchardmeasurement-csv'),
     path('api/trees/filterbylabmeasurementstats/', views.LabMeasurementView.TreesFilteredByLabMeasurementStats.as_view(), name='treesfilteredbylabmeasurementstats-list'),
     path('api/trees/<int:pk>/analytics', views.TreeView.TreeAnalytics.as_view(), name='tree-analytics'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)