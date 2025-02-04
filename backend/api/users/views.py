from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class UserInfosView(RetrieveUpdateAPIView):
    permission_classes=(IsAuthenticated),
    serializer_class=UserSerializer
    
    def get_object(self):
        return self.request.user
