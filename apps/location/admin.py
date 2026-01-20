from django.contrib import admin
from .models import Location

# create location for admin

@admin.register(Location)

class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'coordinateX', 'coordinateY','created_at', 'updates_at']
    search_fields = ['name']
    ordering = ['-updates_at']
    list_filter=['created_at', 'updates_at']
    readonly_fields = ['created_at', 'updates_at']
    
    #mb add id?

