from django.contrib.auth.models import User, Group
from courier_cabinet import models
from rest_framework import serializers
import views


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    responsible = serializers.PrimaryKeyRelatedField(read_only=True)


    class Meta:
        model = models.Order
        fields = ('date', 'responsible')


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('name', 'surname')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
