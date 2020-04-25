from django.shortcuts import render
from accounts.serializers import *
from accounts.models import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class UserListView(generics.ListAPIView):
    serializer_class = UserListSerializer
    queryset = MyUser.objects.all()
    # filter_backends = [DjangoFilterBackend]
    # filter_fields = ['tags']
    permission_classes = [IsAuthenticated]



class UserUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserListSerializer
    queryset = MyUser.objects.all()
    permission_classes = [IsAuthenticated]