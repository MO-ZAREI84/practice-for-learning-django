from django.contrib import admin
from django.urls import path
from cbvapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/',StudentsShow.as_view(),name = 'student'),
    path('student/<int:pk>/',students_detail.as_view(),name = "detail"),
    path('createstudent/',student_create.as_view(),name = "create"),
    path('update/<int:pk>/',student_update.as_view(),name = "update"),
    path('delete/<int:pk>/',student_delete.as_view(),name = "delete"),
]

