
from django.contrib import admin
from django.urls import path
from modelapp.views import Student

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',Student)
]
