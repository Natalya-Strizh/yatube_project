# posts/urls.py
from django.urls import path
from django.urls import include
from . import views
app_name = 'posts'

urlpatterns = [
    path('',  views.index, name = 'índex'),
    path('group_posts/<str:name>/', views.group_posts, name = 'group_post'),
] 