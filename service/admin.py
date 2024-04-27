from django.contrib import admin
from service.models import *
from django.utils import timezone

# Register your models here.


class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'request_type', 'status', 'submit', 'resolved_at')
    list_filter = ('status', 'request_type', 'submit')
    search_fields = ('name', 'request_type', 'details')
    actions = ['mark_resolved']

    def mark_resolved(self, request, queryset):
        queryset.update(status='Resolved')
    mark_resolved.short_description = "Mark selected as resolved"
    
    def mark_resolved(self, request, queryset):
        queryset.update(status='Resolved', resolved_at=timezone.now())
    mark_resolved.short_description = "Mark selected as resolved"

    def save_model(self, request, obj, form, change):
        if obj.status == 'Resolved' and not obj.resolved_at:
            obj.resolved_at = timezone.now()
        obj.save()



admin.site.register(service_request,ServiceRequestAdmin)



