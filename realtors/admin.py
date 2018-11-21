from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ['name','description','email']
    search_fields = ['name']

admin.site.register(Realtor,RealtorAdmin)
