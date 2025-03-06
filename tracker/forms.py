from django import forms
from .models import CarbonEntry, FitnessEntry

class CarbonEntryForm(forms.ModelForm):
    class Meta:
        model = CarbonEntry
        fields = ['travel_km', 'energy_kwh', 'beef_meals', 'chicken_meals', 'veg_meals', 'start_lat', 'start_lng', 'end_lat', 'end_lng']
        widgets = {
            'travel_km': forms.NumberInput(attrs={'step': '0.1'}),
            'energy_kwh': forms.NumberInput(attrs={'step': '0.1'}),
            'beef_meals': forms.NumberInput(),
            'chicken_meals': forms.NumberInput(),
            'veg_meals': forms.NumberInput(),
            'start_lat': forms.NumberInput(attrs={'step': '0.0001'}),
            'start_lng': forms.NumberInput(attrs={'step': '0.0001'}),
            'end_lat': forms.NumberInput(attrs={'step': '0.0001'}),
            'end_lng': forms.NumberInput(attrs={'step': '0.0001'}),
        }

class FitnessEntryForm(forms.ModelForm):
    class Meta:
        model = FitnessEntry
        fields = ['weight', 'waist_size', 'exercise_minutes', 'calories']
        widgets = {
            'weight': forms.NumberInput(attrs={'step': '0.1'}),
            'waist_size': forms.NumberInput(attrs={'step': '0.1'}),
            'exercise_minutes': forms.NumberInput(),
            'calories': forms.NumberInput(),
        }