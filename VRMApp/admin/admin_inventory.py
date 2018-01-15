from django.contrib import admin
from VRMApp.models import *

class PhysicalInvD_Inline(admin.TabularInline):model = PhysicalInvD

@admin.register(PhysicalInvM)
class PhysicalInvMAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['PInvNo','PInvDate','PInvSeq','RegDT','UptDT']
    list_display_links = list_display
    search_fields = ['PInvNo','PInvDate']
    inlines = [PhysicalInvD_Inline]

class InOutD_Inline(admin.TabularInline):model = InOutD

@admin.register(InOutM)
class InOutMAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['InOutNo','InOutDate','InWHSeq','OutWHSeq','RegDT','UptDT']
    list_display_links = list_display
    search_fields = ['InOutNo','InOutDate']
    inlines = [InOutD_Inline]


# class PhysicalInvDAdmin(admin.ModelAdmin):
#     list_display = ['PInvSeq','PInvSerl','SerialNo','RegDT','UptDT']
#     list_display_links = list_display
#     search_fields = ['PInvSeq','SerialNo']

#admin.site.register(PhysicalInvM, PhysicalInvMAdmin)
#admin.site.register(PhysicalInvD, PhysicalInvDAdmin)