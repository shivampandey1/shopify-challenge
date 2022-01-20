from django.urls import path
from . import views

urlpatterns= [
    path('', views.gallery, name ='gallery'),
    path('picture/<str:pk>/', views.viewPicture, name ='picture'),
    path('upload/', views.uploadPicture, name ='upload'),
]