from django.contrib import admin
from django.urls import path
from fiuter.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('hello/',display),
    path('time/', displaydatetime),
]
