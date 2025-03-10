from django.contrib import admin
from django.urls import path
from cookiapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  
    path('about/', views.about, name='about'), 
    path('count/', views.CountView, name='count'),  
]
