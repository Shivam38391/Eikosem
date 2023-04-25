# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from mytodoapp.models import CustomUser


# Create your views here.
class TodoAV(APIView):
    # permission_classes = [permissions.IsAdminUser]
    
    
    def get(self, request):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in CustomUser.objects.all()]
        print(usernames)
        return Response(usernames)