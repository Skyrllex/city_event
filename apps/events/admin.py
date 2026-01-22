from django.contrib import admin
from .models import Event, EventImage


class EventImageInLine(admin.TabularInline):
    model = EventImage
    extra = 1

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name','description','start_date','end_date','top','status']
    list_filter = ['status','start_date','end_date','top']
    search_fields = ['name', 'description','id_location']
    ordering = ['name','start_date','end_date']

    inlines = [EventImageInLine]


@admin.register(EventImage)
class EventImageAdmin(admin.ModelAdmin):
    list_display=['event','image']
    list_filter=['event']