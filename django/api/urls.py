from django.urls import path
from api import views

urlpatterns = [
    path('get/', views.handle_get),
    path('post/', views.handle_post),
    path('put/', views.handle_put),
    path('delete/', views.handle_delete),
    ]
