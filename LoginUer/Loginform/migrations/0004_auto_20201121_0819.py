# Generated by Django 3.1.3 on 2020-11-21 08:19

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('Loginform', '0003_auto_20201121_0815'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='person_details',
            managers=[
                ('persons', django.db.models.manager.Manager()),
            ],
        ),
    ]