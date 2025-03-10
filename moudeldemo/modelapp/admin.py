from django.contrib import admin
from modelapp.models import student

class studentadmin(admin.ModelAdmin):
    list_display= ['firstname','lastname']
admin.site.register(student,studentadmin)
