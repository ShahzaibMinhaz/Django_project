from django.contrib import admin
from .models import profile,invoiceheader,itemdetails

# Register your models here.
admin.site.register(profile)
admin.site.register(invoiceheader)
admin.site.register(itemdetails)
