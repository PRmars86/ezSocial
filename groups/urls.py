from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'groups'

urlpatterns = [
    path("", views.ListGroups.as_view(), name='all'),
    path("new/", views.CreateGroup.as_view(), name='create'),
    path("posts/<slug>/", views.SingleGroup.as_view(), name='single'),
]
