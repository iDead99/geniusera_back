from . import models
from rest_framework import serializers

class TeacherSerializer(serializers.ModelSerializer):
    user_id=serializers.IntegerField(read_only=True)
    # user_id=serializers.IntegerField()
    class Meta:
        model=models.Customer
        fields=['id', 'user_id', 'gender', 'region', 'district', 'town', 'qualification', 'school_level', 'subject', 'phone', 'link', 'amount', 'status']

class StudentSerializer(serializers.ModelSerializer):
    user_id=serializers.IntegerField(read_only=True)
    class Meta:
        model=models.Customer
        fields=['id', 'user_id', 'gender','phone', 'status']

class StatusSerializer(serializers.ModelSerializer):
    user_id=serializers.IntegerField(read_only=True)
    class Meta:
        model=models.Customer
        fields=['id', 'user_id', 'status']