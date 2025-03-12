from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BlogSerializers
from .models import Blogs


# Get all blogs
@api_view(['GET'])
def blog_list(request):
    blogs = Blogs.objects.all()
    serializer = BlogSerializers(blogs, many=True)
    return Response(serializer.data)

# Creaate a new blog
@api_view(['POST'])
def blog_create(request):
    if request.method =="POST":
        serializer = BlogSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)