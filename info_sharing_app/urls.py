from django.urls import path
from . import views

urlpatterns = [
    path('', views.info_list, name='info_list'),
    path('readme/', views.readme, name='readme'),
    path('info/<int:pk>/', views.info_detail, name='info_detail'),
    path('info/new/', views.info_new, name='info_new'),
    path('info/<int:pk>/edit/', views.info_edit, name='info_edit'),
    path('info/<int:pk>/remove/', views.info_remove, name='info_remove'),
    path('info/<int:pk>/add_comment/', views.add_comment, name='add_comment'),
]