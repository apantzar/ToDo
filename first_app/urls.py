from django.urls import path
from . import views

urlpatterns = [

    path('edit/<int:id>/', views.edit, name='edit'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('add/', views.add, name='add'),
    path('save_edit/<int:id>', views.save_edit, name='save_edit'),

]

