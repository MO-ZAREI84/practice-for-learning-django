
from django.contrib import admin
from django.urls import path

from formapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/' , registerf ),
]
