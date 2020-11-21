from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver,Signal
from .models import profile,invoiceheader,itemdetails
from . import signals

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print('krwags :',kwargs)
    if created:
        profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

# @receiver(post_save,sender=invoiceheader)
Itemdetailssave = Signal(providing_args=['tabledata','Invoice','created'])

@receiver(Itemdetailssave)
def add_Item_In_Tables(sender, **kwargs):
    if kwargs['created']:
        for i in range(len(kwargs['tabledata'])):
            # print('entry No ',i)
            productName = kwargs['tabledata'][i]['productName']
            productQuantity = kwargs['tabledata'][i]['productQuantity']
            productPrice = kwargs['tabledata'][i]['productPrice']
            print(productName," ",productQuantity," ",productPrice)
            item_details = itemdetails.objects.create(Item_Name=productName,Item_quentity=productQuantity,Item_Price=productPrice,Invoice_header=kwargs['Invoice'])
            item_details.save()
            print('Item Saved')