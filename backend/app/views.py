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

# Get a single blog
@api_view(['GET'])
def blog_detail(request, pk):
    try:
        blog = Blogs.objects.get(id=pk)
    except Blogs.DoesNotExist:
        return Response({"error": "Blog not found"})    
    serializer = BlogSerializers(blog, many=False)
    return Response(serializer.data)

# Creaate a new blog
@api_view(['POST'])
def blog_create(request):
    if request.method =="POST":
        serializer = BlogSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

# complete update a blog
@api_view(['PUT'])
def blog_complete_update(request, pk):
    if request.method == 'PUT':
        try:
            blog = Blogs.objects.get(id=pk)    
            serializer = BlogSerializers(instance=blog, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)})   
        
# partial update a blog
@api_view(['PATCH'])
def blog_partial_update(request, pk):
    if request.method == 'PATCH':
        try:
            blog = Blogs.objects.get(id=pk)    
            serializer = BlogSerializers(instance=blog, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}) 