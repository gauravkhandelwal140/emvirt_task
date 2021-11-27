from django.contrib import admin
from django.contrib.auth.models import Group

from .models import *
# Register your models here.
admin.site.unregister(Group)
admin.site.site_title='IOT Project'
admin.site.site_header='Iot Project'
admin.site.index_title='Iot Project'
class DeviceAdmin(admin.ModelAdmin):
    list_display=('id','uptime','memory_usage','is_active','user')

class DiskpartitionInfoAdmin(admin.ModelAdmin):
    list_display = ('device', 'info',)

admin.site.register(Device,DeviceAdmin)
admin.site.register(Diskpartitioninfo,DiskpartitionInfoAdmin)