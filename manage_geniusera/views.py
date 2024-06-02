from django.shortcuts import render
from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import action
from . import models
from . import serializers
# from core.serializers import CustomUserSerializer
# from core.models import User


class TeacherViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=models.Customer.objects.filter(status='Teacher').order_by('region')
    serializer_class=serializers.TeacherSerializer
    # permission_classes=[permissions.IsAuthenticated]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[permissions.IsAuthenticated])
    def me(self, request):
        teacher=models.Customer.objects.get(user_id=request.user.id)
        if request.method=='GET':
            serializer=serializers.TeacherSerializer(teacher)
            return Response(serializer.data)
        elif request.method=='PUT':
            serializer=serializers.TeacherSerializer(teacher, data=request.data)
            serializer.is_valid()
            serializer.save()
            return Response(serializer.data)
        
class StudentViewSet(ModelViewSet):
    queryset=models.Customer.objects.all()
    serializer_class=serializers.StudentSerializer
    # permission_classes=[permissions.IsAdminUser]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[permissions.IsAuthenticated])
    def me(self, request):
        student=models.Customer.objects.get(user_id=request.user.id)
        if request.method=='GET':
            serializer=serializers.StudentSerializer(student)
            return Response(serializer.data)
        elif request.method=='PUT':
            serializer=serializers.StudentSerializer(student, data=request.data)
            serializer.is_valid()
            serializer.save()
            return Response(serializer.data)
        

# class TeacherUserViewSet(viewsets.ReadOnlyModelViewSet):
#     serializer_class = CustomUserSerializer

#     def get_queryset(self):
#         return User.objects.filter(customer__status='Teacher')

#     def retrieve(self, request, pk=None):
#         teacher = self.get_object()
#         serializer = CustomUserSerializer(teacher)
#         return Response(serializer.data)



class SearchViewSet(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.TeacherSerializer

    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.GET.get('q', '')
        if query:
            results = models.Customer.objects.filter(
                Q(region__icontains=query) | Q(district__icontains=query) |
                Q(town__icontains=query) | Q(subject__icontains=query)
            ).order_by('region')
            serializer = serializers.TeacherSerializer(results, many=True)
            return Response(serializer.data)
        return Response([])
    
    def retrieve(self, request, pk=None):
        teacher = self.get_object()
        serializer = serializers.TeacherSerializer(teacher)
        return Response(serializer.data)


class StatusViewSet(ModelViewSet):
    queryset=models.Customer.objects.all()
    serializer_class=serializers.StatusSerializer
    # permission_classes=[permissions.IsAdminUser]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[permissions.IsAuthenticated])
    def status(self, request):
        status=models.Customer.objects.get(user_id=request.user.id)
        if request.method=='GET':
            serializer=serializers.StatusSerializer(status)
            return Response(serializer.data)
        elif request.method=='PUT':
            serializer=serializers.StatusSerializer(status, data=request.data)
            serializer.is_valid()
            serializer.save()
            return Response(serializer.data)