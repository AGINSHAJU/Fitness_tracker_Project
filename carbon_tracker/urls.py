from django.contrib import admin
from django.urls import path, include
from tracker import views  # Import views from your tracker app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Handles login, signup, etc.
    path('', include('tracker.urls')),  # Root URL goes to tracker app
    path('contactus/', views.contactus, name='contactus'),  # Add contact page URL
    path('profile/', views.profile, name='profile'),
    path('aboutus/', views.aboutus, name='aboutus'),  # Add contact page URL
    path('fitness/add/', views.fitness_add_entry, name='fitness_add_entry'),
]
