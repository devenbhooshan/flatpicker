from django.contrib import admin

from Core.models import *

class FlatAdmin(admin.ModelAdmin):
	list_filter=['approved','location','bhk']
	list_display=['approved','url','title','price','bhk','size']
	list_editable=['approved']

class LCCAdmin(admin.ModelAdmin):
	list_filter=['city','location','company']

class LLAdmin(admin.ModelAdmin):
	list_filter=['company','city','area']


admin.site.register(City)
admin.site.register(BHK)
admin.site.register(Company)
admin.site.register(Flat,FlatAdmin)
admin.site.register(Location)
admin.site.register(LocationCompanyCity,LCCAdmin)
admin.site.register(Area)
admin.site.register(LatLong,LLAdmin)
# Register your models here.
