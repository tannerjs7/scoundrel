from django.urls import path
from . import views


app_name = 'scoundrel'
urlpatterns = [
    path('index/', views.index, name='index')
]