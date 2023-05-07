from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Post
from .serializers import PostSerializer
from rest_framework.parsers import MultiPartParser, FormParser



class PostPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = PostPagination

class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostLikeView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        post = self.get_object()
        user = request.user

        if user in post.likes.all():
            post.likes.remove(user)
            return Response({'detail': 'Post unliked.'})
        else:
            post.likes.add(user)
            return Response({'detail': 'Post liked.'})

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = generics.get_object_or_404(queryset, pk=self.kwargs['pk'])
        return obj
