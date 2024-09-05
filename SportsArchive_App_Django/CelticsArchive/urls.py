# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='CelticsArchive_home'),
    path('create/', views.create_legendary_moment, name='create_legendary_moment'),
    path('legendary_moments/', views.legendary_moments_list, name='legendary_moments_list'),
    path('moments/<int:id>/', views.legendary_moment_detail, name='legendary_moment_detail'),
]