from django.contrib import admin
from django.urls import path
from  .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('mobiles/', mobiles),
    path('laptops/', laptops),
    path('gadgets/', gadgets),
    
]

