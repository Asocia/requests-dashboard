from django.urls import path
from . import views
from . import dashboard  # this line is required even if it is not used here

urlpatterns = [
    path('', views.home, name='home')
]
