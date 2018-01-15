from django.contrib import admin
from VRMApp.models import *

class EmpWorkPlanAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['WorkDate','EmpSeq','StrDate','StrTime','EndDate','EndTime','RegDT','UptDT']
    list_display_links = list_display
    search_fields = ['WorkDate','EmpSeq']

class EmpWorkRptAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['WorkDate','EmpSeq','StrDate','StrTime','EndDate','EndTime','RegDT','UptDT']
    list_display_links = list_display
    search_fields = ['WorkDate','EmpSeq']

class PlayPlanAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['PlayDate','PlayOrder','PlaySerl','StrTime','EndTime','RegDT','UptDT']
    list_display_links = list_display
    search_fields = ['PlayDate','PlayOrder']

admin.site.register(EmpWorkPlan, EmpWorkPlanAdmin)
admin.site.register(EmpWorkRpt, EmpWorkRptAdmin)
admin.site.register(PlayPlan, PlayPlanAdmin)
admin.site.register(Post)
