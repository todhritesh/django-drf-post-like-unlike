from django.urls import path
from .views import PostListView, PostCreateView, PostLikeView

app_name = 'post'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/like/', PostLikeView.as_view(), name='post_like'),
]