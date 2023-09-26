from django.contrib import admin
from website.models import Contact 
from .models import Post

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name','sender','created_date')
    list_filter = ('sender',)
    search_fields = ('name','message')


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('title','status','created_date','id')
    list_filter = ('published_date',)
    search_fields = ('title',)

admin.site.register(Contact,ContactAdmin)
admin.site.register(Post,PostAdmin)