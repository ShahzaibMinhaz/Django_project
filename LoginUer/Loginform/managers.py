from django.db import models


class CustomManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().order_by('id')
    
    def get_person_by_id(self,r1,r2):
        return super().get_queryset().filter(id__range=(r1,r2))