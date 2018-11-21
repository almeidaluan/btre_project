from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_publisehd','price','list_date','realtor')
    search_fields = ['title','price','realtor']
    autocomplete_fields = ['realtor']
    

admin.site.register(Listing,ListingAdmin)
