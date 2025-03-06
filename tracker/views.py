from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CarbonEntry, UserProfile,FitnessEntry
from .forms import CarbonEntryForm,FitnessEntryForm
import plotly.graph_objects as go
import json

@login_required
def dashboard(request):
    entries = CarbonEntry.objects.filter(user=request.user)
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    dates = [entry.date for entry in entries]
    co2_values = [entry.co2_emitted for entry in entries]
    fig = go.Figure(data=go.Scatter(x=dates, y=co2_values, mode='lines+markers'))
    chart = fig.to_html(full_html=False)
    recommendation = predict_recommendation(entries)

    # Prepare travel locations for the map
    travel_locations = [
        {
            'start': {'lat': entry.start_lat, 'lng': entry.start_lng},
            'end': {'lat': entry.end_lat, 'lng': entry.end_lng},
            'co2': entry.co2_emitted
        }
        for entry in entries if entry.start_lat and entry.end_lat
    ]

    context = {
        'entries': entries,
        'points': profile.points,
        'badges': profile.badges,
        'chart': chart,
        'recommendation': recommendation,
        'google_maps_api_key': 'AIzaSyDWBx3gBxJ3NTqJcprVxW77sa8kbXOBMNg',
        'travel_locations': json.dumps(travel_locations)  # Pass as JSON
    }
    return render(request, 'tracker/dashboard.html', context)

@login_required
def add_entry(request):
    if request.method == 'POST':
        form = CarbonEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            profile = UserProfile.objects.get(user=request.user)
            profile.award_points(10)
            return redirect('dashboard')
    else:
        form = CarbonEntryForm()
    return render(request, 'tracker/add_entry.html', {'form': form})

def predict_recommendation(entries):
    if not entries:
        return "Start tracking to get personalized tips!"
    total_co2 = sum(entry.co2_emitted for entry in entries)
    if total_co2 > 50:
        return "Try reducing car travel by 20% to save 10kg CO2 this week!"
    return "Great job! Keep up your low-impact habits."

def contactus(request):
    return render(request, 'contactus.html')

def aboutus(request):
    return render(request, 'aboutus.html')
def front_page(request):
    return render(request, 'front_page.html')

@login_required
def profile(request):
    profile = UserProfile.objects.get(user=request.user)
    return render(request, 'tracker/profile.html', {'profile': profile})
@login_required
def fitness_dashboard(request):
    entries = FitnessEntry.objects.filter(user=request.user)
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    dates = [entry.date for entry in entries]
    weights = [entry.weight for entry in entries]
    fig = go.Figure(data=go.Scatter(x=dates, y=weights, mode='lines+markers', name='Weight (kg)'))
    chart = fig.to_html(full_html=False)
    health_status = get_fitness_health_status(entries, profile)

    context = {
        'entries': entries,
        'points': profile.points,
        'badges': profile.badges,
        'chart': chart,
        'health_status': health_status,
    }
    return render(request, 'tracker/fitness_dashboard.html', context)

@login_required
def fitness_add_entry(request):
    if request.method == 'POST':
        form = FitnessEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            profile = UserProfile.objects.get(user=request.user)
            profile.award_points(10)
            return redirect('fitness_dashboard')
    else:
        form = FitnessEntryForm()
    return render(request, 'tracker/fitness_add_entry.html', {'form': form})

def get_fitness_health_status(entries, profile):
    if not entries:
        return "Start tracking to assess your health!"
    latest_entry = entries.latest('date')
    bmi = latest_entry.bmi
    if bmi < 18.5:
        return "Underweight - Consider consulting a nutritionist."
    elif 18.5 <= bmi < 25:
        return "Healthy weight - Keep up the good work!"
    elif 25 <= bmi < 30:
        return "Overweight - Increase exercise and monitor diet."
    else:
        return "Obese - Consult a doctor for health advice."
