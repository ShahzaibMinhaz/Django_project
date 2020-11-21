from django.db import models
from django.contrib.auth.models import User
from .managers import CustomManager

class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to="profile_pics")

    def __str__(self):
        return self.user.username


class invoiceheader(models.Model):
    Name = models.CharField(max_length=100)
    Total_Price = models.IntegerField()

class itemdetails(models.Model):
    Item_Name = models.CharField(max_length=100)
    Item_quentity = models.CharField(max_length=100)
    Item_Price = models.IntegerField()
    Invoice_header = models.ForeignKey(invoiceheader, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Item_Name)

'''model managers Practice'''



class Person_details(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    persons = models.Manager()
    personorder = CustomManager()


