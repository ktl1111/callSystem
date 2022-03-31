from django.db import models
from datetime import datetime
# Create your models here.


class Number(models.Model):
    num = models.IntegerField(default=0)
    stamp = models.DateTimeField(default=datetime.now, blank=True)

class OnspotNum(models.Model):
    onspot_num = models.IntegerField(default=0)
    onspot_stamp = models.DateTimeField(default=datetime.now, blank=True)

