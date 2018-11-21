from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_published','price','list_date','realtor')
    list_display_links = ('id','title')
    list_filter = ('list_date','price',)
    list_editable = ('is_published',)
    search_fields = ['title','description','address','city','state','zipcode','price']
    list_per_page = 25
    autocomplete_fields = ['realtor']
    

admin.site.register(Listing,ListingAdmin)
