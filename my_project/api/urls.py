from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostsView.as_view(), name='get_posts'),
    path('posts/<str:id>', views.GetPost.as_view(), name='get_post'),
]