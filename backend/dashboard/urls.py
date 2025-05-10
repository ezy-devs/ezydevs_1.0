from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('testimonials/', views.testimonials_dashboard, name='testimonials_dashboard'),
    path('testimonials/add/', views.add_testimony, name='add_testimony'),
    path('testimonials/edit/<uuid:id>/', views.edit_testimony, name='edit_testimony'),
    path('testimonials/delete/<uuid:id>/', views.delete_testimony, name='delete_testimony'),
]