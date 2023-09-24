from django.contrib import admin
from website.models import Contact 

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name','sender','created_date')
    list_filter = ('sender',)
    search_fields = ('name','message')

admin.site.register(Contact,ContactAdmin)

