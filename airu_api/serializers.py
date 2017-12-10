from django.contrib.auth.models import User, Group
from airu_api import models
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Device
        fields = ('id', 'owner', 'latitude', 'longitude', 'firmware_ver', 'device_revision')
