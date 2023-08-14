#  импортируйте в код всё необходимое
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import PostSerializer
from .models import Post
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework import status


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticatedOrReadOnly,))
def api_posts(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT', 'PATCH', 'DELETE'])
@permission_classes((IsAuthenticatedOrReadOnly,))
def api_posts_detail(request, id):
    post = get_object_or_404(Post,id=id)
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data, status = status.HTTP_200_OK)
    elif request.method == 'PUT' or request.method == 'PATCH':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.author = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        post.delete()
        return Response({'message': f'Post {id} deleted' }, status=status.HTTP_301_MOVED_PERMANENTLY)
