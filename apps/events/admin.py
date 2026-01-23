from django.contrib import admin
from .models import Event, EventImage

class EventImageInLine(admin.TabularInline):
    model = EventImage
    extra = 1

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name','description','start_date','end_date','top','status']
    
    list_filter = ['status','start_date','end_date','top']
    search_fields = ['name', 'description']
    ordering = ['name','start_date','end_date']
    readonly_fields=['author']
    inlines = [EventImageInLine]
    def save_model(self, request, obj, form, change):
        if not obj.pk:    
            obj.author = request.user
        return super().save_model(request, obj, form, change)

@admin.register(EventImage)
class EventImageAdmin(admin.ModelAdmin):
    list_display=['event','image']
    list_filter=['event']

    