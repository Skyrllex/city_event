from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name','description', 'start_date','end_date','top','status']
    list_filter = ['status','start_date','end_date','top']
    search_fields = ['name', 'description']
    ordering = ['name','start_date','end_date']