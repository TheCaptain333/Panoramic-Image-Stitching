from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name = 'upload-image'),
    path('download/<int:image_id>/', views.download, name = 'download-image')
]