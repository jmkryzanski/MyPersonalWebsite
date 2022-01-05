from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('myblog/', views.myblog, name="myblog"),
    path('myblog/<int:id>', views.myblog2, name="myblog2"),
    path('myblog/<int:id>/update', views.updatePost, name="updatePost"),
    path('contact', views.contact, name="contact"),
    path('addPost', views.addPost, name="addPost"),
    path('deletePost/<int:id>', views.deletePost, name="deletePost"),
]
