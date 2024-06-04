from django.db import router
from django.urls import path
from .import views






urlpatterns = [

    path('success/', views.success, name='success'),  


    path('school_list/', views.school_list, name='school_list'),
    path('add_school/', views.add_school, name='add_school'),
    path('school/<int:school_id>/delete/', views.school_delete, name='school_delete'),
    path('school/<int:school_id>/update/', views.school_update, name='school_update'),
    path('school_detail/<int:school_id>/', views.school_detail, name='school_detail'),
]

    
