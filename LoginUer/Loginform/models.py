from django.db import models
from django.contrib.auth.models import User

class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to="profile_pics")

    def __str__(self):
        return self.user.username


class invoiceheader(models.Model):
    Invoice_Number = models.IntegerField(max_length=None,primary_key=True)
    Name = models.CharField(max_length=100)
    Total_Price = models.IntegerField()

    def __str__(self):
        return str(self.Invoice_Number)

class itemdetails(models.Model):
    Item_Name = models.CharField(max_length=100)
    Item_quentity = models.CharField(max_length=100)
    Item_Price = models.IntegerField()

    def __str__(self):
        return str(self.Item_Name)


