from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import action
from . import models
from . import serializers

class TeacherUserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.CustomUserSerializer

    def get_queryset(self):
        return models.User.objects.filter(customer__status='Teacher')

    def retrieve(self, request, pk=None):
        teacher = self.get_object()
        serializer = serializers.CustomUserSerializer(teacher)
        return Response(serializer.data)
    
        
class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.CustomUserSerializer
    
    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[permissions.IsAuthenticated])
    def me(self, request):
        user = request.user
        if request.method=='GET':
            serializer=self.get_serializer(user)
            return Response(serializer.data)
        elif request.method=='PUT':
            serializer=self.get_serializer(user, data=request.data, partial=True)
            serializer.is_valid()
            serializer.save()
            return Response(serializer.data)