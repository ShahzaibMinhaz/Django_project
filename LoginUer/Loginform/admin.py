from django.contrib import admin
from .models import profile,invoiceheader,itemdetails,Person_details

# Register your models here.
admin.site.register(profile)
admin.site.register(invoiceheader)

@admin.register(itemdetails)
class details(admin.ModelAdmin):
    list_display = ['id','Item_Name','Item_quentity','Item_Price','Invoice_header']

@admin.register(Person_details)
class person(admin.ModelAdmin):
    list_display = ['id','firstName','lastName']
# admin.site.register(itemdetails)
