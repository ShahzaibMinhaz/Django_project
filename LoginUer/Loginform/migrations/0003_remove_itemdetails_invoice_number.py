# Generated by Django 3.1.3 on 2020-11-18 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Loginform', '0002_itemdetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemdetails',
            name='Invoice_Number',
        ),
    ]
