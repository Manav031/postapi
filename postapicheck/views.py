from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PostSerializer
from .models import Post
from rest_framework.status import *
# Create your views here.


class CheckPost(APIView):
    def get(self,request):
        data = {}
        posts = Post.objects.all()
        for i in posts:
            if i.isvalid == False:
                i.notification = "You're Post is in pending state"
                i.save()
            else:
                i.notification = ""
                i.save()
                
        return Response({"messae":"success"})