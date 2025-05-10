from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('projects/', views.projects, name='projects'),
    path('team/', views.team, name='team'),
    path('testimonials/', views.testimonials, name='testimonials'),
    # path('blog/', views.blog, name='blog'),
    # path('blog/<int:post_id>/', views.blog_detail, name='blog_detail'),
    # path('blog/new/', views.new_post, name='new_post'),

] 