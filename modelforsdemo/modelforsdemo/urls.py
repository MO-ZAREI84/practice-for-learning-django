
from django.contrib import admin
from django.urls import path
from modelforms import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('listProjects', views.listproject),
    path('addProject', views.addProject),
]
