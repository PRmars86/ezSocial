from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'posts'

urlpatterns = [
    path("", views.PostList.as_view(), name='all'),
    path("new/", views.CreatePost.as_view(), name='create'),
    path("by/<str:username>/", views.UserPosts.as_view(), name='for_user'),
    path("by/<str:username>/<str:pk>/",
         views.PostDetail.as_view(), name='single'),
    path("delete/<str:pk>/", views.DeletePost.as_view(), name='delete'),
]
