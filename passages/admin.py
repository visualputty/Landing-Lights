from passages.models import Passage, VesselDetail
from django.contrib import admin

class PassageAdmin(admin.ModelAdmin):
    list_display = ('etd_sharpness', 'ship_name', 'date_added')
    list_filter = ['etd_sharpness']
    search_fields = ['ship_name']

class VesselDetailAdmin(admin.ModelAdmin):
    list_display = ('ship_name', 'imo', 'email_address')
    search_fields = ['ship_name']
    
admin.site.register(Passage, PassageAdmin)
admin.site.register(VesselDetail, VesselDetailAdmin)