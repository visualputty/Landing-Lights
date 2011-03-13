from passages.models import Passage, VesselDetail
from django.contrib import admin

class PassageAdmin(admin.ModelAdmin):
    list_display = ('eta_breaksea', 'ship_name', 'dock_pilot', 'email_address',  'date_added')
    search_fields = ['ship_name']
    fieldsets = (
        (None, {
            'fields': ('ship_name', 'eta_breaksea', 'etd_sharpness', 'email_address', 'dock_pilot')
        }),
        ('Further info', {
            'classes': ('collapse',),
            'fields': ('speed', 'bowthrust', 'radar', 'fwd_draft', 'aft_draft', 'other', 'no_persons',
                       'next_port')
        }),
        ('Vessel info', {
            'classes': ('collapse',),
            'fields': ('imo', 'dwt', 'max_loa', 'max_beam', 'height', 'rudder')
        }),
    )
    ordering = ('-eta_breaksea','ship_name')

class VesselDetailAdmin(admin.ModelAdmin):
    list_display = ('ship_name', 'imo')
    search_fields = ['ship_name']
    
admin.site.register(Passage, PassageAdmin)
admin.site.register(VesselDetail, VesselDetailAdmin)