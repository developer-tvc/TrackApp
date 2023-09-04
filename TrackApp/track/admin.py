from django.contrib import admin
from .models import Worker, Unit, Visit


class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number')
    search_fields = ['name']

class UnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'worker')
    search_fields = ['name']

class VisitAdmin(admin.ModelAdmin):
    list_display = ('visit_date', 'longitude', 'latitude', 'get_visitor', 'get_unit')
    search_fields = ['unit__name', 'unit__worker__name']

    @admin.display(description='Visitor')
    def get_visitor(self, obj):
        return obj.unit.worker.name

    @admin.display(description='Unit')
    def get_unit(self, obj):
        return obj.unit.name
    
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Worker, WorkerAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Visit, VisitAdmin)
