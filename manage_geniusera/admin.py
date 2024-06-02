from django.contrib import admin
from .import models

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    autocomplete_fields = ['user']
    list_display=['first_name', 'last_name', 'status']
    list_per_page=10
    list_select_related=['user']
    ordering=['user__first_name', 'user__last_name']
    search_fields=['first_name__istartswith', 'last_name__istartswith']

# @admin.register(models.Student)
# class StudentAdmin(admin.ModelAdmin):
#     autocomplete_fields = ['user']
#     list_display=['first_name', 'last_name']
#     list_per_page=10
#     list_select_related=['user']
#     ordering=['user__first_name', 'user__last_name']
#     search_fields=['first_name__istartswith', 'last_name__istartswith']
