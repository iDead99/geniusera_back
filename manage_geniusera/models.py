from django.db import models
from django.conf import settings
from django.contrib import admin

class Customer(models.Model):
    gender=models.CharField(max_length=10)
    region=models.CharField(max_length=255)
    district=models.CharField(max_length=255)
    town=models.CharField(max_length=255)
    qualification=models.CharField(max_length=255)
    school_level=models.TextField()
    subject=models.TextField()
    phone=models.CharField(max_length=50)
    link=models.CharField(max_length=500, null=True, blank=True)
    amount=models.DecimalField(max_digits=6, decimal_places=2, default=0)
    status=models.CharField(max_length=255)
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'

    @admin.display(ordering='user__last_name')
    def first_name(self):
        return self.user.first_name
    
    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name
    
    class Meta:

        ordering=['user__first_name', 'user__last_name']

# class Student(models.Model):
#     phone=models.CharField(max_length=50)
#     user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

#     def __str__(self) -> str:
#         return f'{self.user.first_name} {self.user.last_name}'

#     @admin.display(ordering='user__last_name')
#     def first_name(self):
#         return self.user.first_name
    
#     @admin.display(ordering='user__last_name')
#     def last_name(self):
#         return self.user.last_name
    
#     class Meta:
#         ordering=['user__first_name', 'user__last_name']
