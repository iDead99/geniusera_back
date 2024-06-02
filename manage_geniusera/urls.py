from rest_framework import routers
from django.urls import path, include
from .import views

router = routers.DefaultRouter()
router.register('teachers', views.TeacherViewSet, basename='teacher')
router.register('students', views.StudentViewSet, basename='student')
# router.register('teacher_users', views.TeacherUserViewSet, basename='teacher_user')
router.register('teacher_searches', views.SearchViewSet, basename='search')
router.register('user_status', views.StatusViewSet, basename='status')
# router.register('update-balance', views.UpdateBalanceViewSet, basename='update-balance')
# router.register('checkbox', views.CheckBoxViewSet, basename='checkbox')
urlpatterns=router.urls