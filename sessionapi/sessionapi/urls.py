
from django.contrib import admin
from django.urls import path,include
from sessionapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.sessionapi),
    path('addItem/',views.AddItem),
    path('displayItems/',views.DisplayItem),
    path('index/',views.index),
]
