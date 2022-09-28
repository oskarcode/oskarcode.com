

from django.urls import path
from .views import PostListView, PostDetailView,PostCreateView, PostUpdateView,PostDeletelView,UserPostListView
from . import views # import views.py models so that we can use functions/classed defined in views.py


urlpatterns = [
    path("", PostListView.as_view(), name = 'blog-home'), # '' is the empty path. PostListView.as_view() is the funnction triggered with this path. name is the name of path, we use it as a reverse path look up later.  
    path("user/<str:username>", UserPostListView.as_view(), name = 'user-posts'),
    path("post/<int:pk>/", PostDetailView.as_view(), name = 'post-detail'),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name = 'post-update'),
    path("post/<int:pk>/delete/", PostDeletelView.as_view(), name = 'post-delete'),
    path("post/new/", PostCreateView.as_view(), name = 'post-create'),
    path("about/", views.about, name = 'blog-about'),
]
