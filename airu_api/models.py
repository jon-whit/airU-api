from django.db import models
from django.contrib.auth.models import User

class Device(models.Model):
    id = models.CharField(db_column='Device ID', max_length=12, primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.DecimalField(db_column='Latitude', max_digits=10, decimal_places=8, null=False)
    longitude = models.DecimalField(db_column='Longitude', max_digits=11, decimal_places=8, null=False)
    firmware_ver = models.CharField(db_column='Firmware Version', max_length=12, null=False)
    device_revision = models.CharField(db_column='Device Revision', max_length=12, null=False)
