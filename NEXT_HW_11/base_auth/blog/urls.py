from django.urls import path
from . import views
from .views import profile, subscribe, unsubscribe
urlpatterns = [
    path('new/', views.new, name='new'),
    path('', views.list, name='list'),
    path('detail/<int:article_id>/', views.detail, name='detail'),
    path('edit/<int:article_id>/', views.edit, name='edit'),
    path('delete/<int:article_id>/', views.delete, name='delete'),
    path('delete-comment/<int:article_id>/<int:comment_pk>/', views.delete_comment, name='delete-comment'),
    path('profile/<str:username>/', profile, name='profile'),
    path('subscribe/<str:username>/', subscribe, name='subscribe'),
    path('unsubscribe/<str:username>/', unsubscribe, name='unsubscribe'),
]