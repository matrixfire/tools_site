
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('index1/', views.index1, name='index1'),
    # Add other paths here
    path("index2/", views.index2, name="index2"),
    path("sections/<int:num>", views.section, name="section"),
    path("index3/", views.index3, name="index3"),
    path("posts", views.posts, name="posts"),
]
