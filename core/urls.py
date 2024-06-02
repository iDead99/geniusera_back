from rest_framework import routers
from django.urls import path, include
from .import views

router = routers.DefaultRouter()
router.register('teacher_users', views.TeacherUserViewSet, basename='teacher_user')
router.register('users', views.UserViewSet, basename='user')
urlpatterns=router.urls