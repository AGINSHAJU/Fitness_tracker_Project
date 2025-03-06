from django.urls import path
from . import views

urlpatterns = [
    # Front Page
    path('', views.front_page, name='front_page'),
    # Carbon Tracker URLs
    path('carbon/', views.dashboard, name='dashboard'),
    path('carbon/add/', views.add_entry, name='add_entry'),
    # Fitness Tracker URLs
    path('fitness/', views.fitness_dashboard, name='fitness_dashboard'),
    path('fitness/add/', views.fitness_add_entry, name='fitness_add_entry'),
    # Shared
    path('about-us/', views.aboutus, name='aboutus'),
]