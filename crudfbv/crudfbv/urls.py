
from django.contrib import admin
from django.urls import path,include
from fbvApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',getstudent,name = 'home'),
    path('create/',createstudent,name = 'create'),
    path('delete/<int:id>/',deletstudent,name = 'del'),
    path('Up/<int:id>/',updatestudent,name = 'UP'),
    path("accounts/", include("django.contrib.auth.urls")),
    path("logout/",logout,name = 'logout')

]
