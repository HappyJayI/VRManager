from django.contrib import admin
from VRMApp.models import *

class MCodeAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['MCodeNo','MCodeName','RegDT','UptDT']
    list_display_links = list_display
    search_fields = ['MCodeNo','MCodeName']

class DCodeAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['DCodeName','RegDT','UptDT']
    list_display_links = list_display
    search_fields = ['DCodeName']

class ItemAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['ItemTypeSeq','ModelSeq','SerialNo','RegDT','UptDT']
    list_display_links = list_display
    search_fields = ['SerilNo']

class WHAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['WHNo','WHName','RegDT','UptDT']
    search_fields = ['WHNo','WHName']

class EmpAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['WorkCompany','EmpNo','EmpName','RegDT','UptDT']
    list_display_links = list_display
    search_fields = ['EmpNo','EmpName']

class CustAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['CustNo','CustName','RegDT','UptDT']
    list_display_links = list_display
    search_fields = ['CustNo','CustName']

class ContentsAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['ContentsNo','ContentsName','ContentsEngName','FileName','RegDT','UptDT']
    list_display_links = list_display
    search_fields = ['ContentsNo','ContentsName']

admin.site.register(MCode, MCodeAdmin)
admin.site.register(DCode, DCodeAdmin)
admin.site.register(WH, WHAdmin)
admin.site.register(Emp, EmpAdmin)
admin.site.register(Cust, CustAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Contents, ContentsAdmin)