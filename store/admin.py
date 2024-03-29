from django.contrib import admin
from . models import Design
from django.utils.html import format_html



# Register your models here.

class DesignAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;"/>'.format(object.design_photo.url))
    
    
    thumbnail.short_description = 'Design Image'
    list_display = ('id', 'thumbnail', 'design_title', 'is_featured')
    list_display_links = ('id', 'thumbnail', 'design_title')
    list_editable= ('is_featured',)





admin.site.register(Design, DesignAdmin)