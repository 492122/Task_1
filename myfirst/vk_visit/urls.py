from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:group_name>/', views.index, name='index'),
]
#vk_visit/<str:group_name>/