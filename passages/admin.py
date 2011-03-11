from passages.models import Passage, VesselDetail
from django.contrib import admin

class PassageAdmin(admin.ModelAdmin):
    list_display = ('eta_breaksea', 'ship_name', 'date_added')
    list_filter = ['eta_breaksea']
    search_fields = ['ship_name']

class VesselDetailAdmin(admin.ModelAdmin):
    list_display = ('ship_name', 'imo')
    search_fields = ['ship_name']
    
admin.site.register(Passage, PassageAdmin)
admin.site.register(VesselDetail, VesselDetailAdmin)