from django.urls import path, re_path
from . import views

app_name = 'app_'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.posts, name='posts'),
    path('posts/<int:id>/', views.post, name='post'),
    path('post/edit/<int:id>/', views.edit, name='edit'),
    path('post/new/', views.new, name='new'),
    path('post/delete/<int:id>', views.delete, name='delete')
]
