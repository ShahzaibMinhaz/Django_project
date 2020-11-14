from django.db import models
from django.contrib.auth.models import User

class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to="profile_pics")

    def __str__(self):
        return self.user.username

class currency(models.Model):
    CountryName = models.CharField(max_length=20,primary_key=True)
    CurrencyValue = models.IntegerField()

    def __str__(self):
        return self.CountryName

class currency(models.Model):
    Name = models.CharField(max_length=20,primary_key=True)
    DOB = models.DateField(auto_now=True)

    def __str__(self):
        return self.CountryName


