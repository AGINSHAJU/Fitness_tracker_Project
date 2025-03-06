from django.db import models
from django.contrib.auth.models import User

# Carbon Tracker Models
class CarbonEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    travel_km = models.FloatField(default=0, help_text="Distance traveled in km")
    energy_kwh = models.FloatField(default=0, help_text="Energy used in kWh")
    beef_meals = models.IntegerField(default=0, help_text="Number of beef-based meals")
    chicken_meals = models.IntegerField(default=0, help_text="Number of chicken-based meals")
    veg_meals = models.IntegerField(default=0, help_text="Number of vegetarian meals")
    co2_emitted = models.FloatField(default=0, help_text="Calculated CO2 in kg")
    start_lat = models.FloatField(null=True, blank=True, help_text="Starting latitude")
    start_lng = models.FloatField(null=True, blank=True, help_text="Starting longitude")
    end_lat = models.FloatField(null=True, blank=True, help_text="Ending latitude")
    end_lng = models.FloatField(null=True, blank=True, help_text="Ending longitude")

    def calculate_co2(self):
        travel_co2 = self.travel_km * 0.12
        energy_co2 = self.energy_kwh * 0.4
        diet_co2 = (self.beef_meals * 5.4) + (self.chicken_meals * 1.2) + (self.veg_meals * 0.5)
        return travel_co2 + energy_co2 + diet_co2

    def save(self, *args, **kwargs):
        self.co2_emitted = self.calculate_co2()
        super().save(*args, **kwargs)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    badges = models.JSONField(default=list)

    def award_points(self, points):
        self.points += points
        if self.points >= 100 and "Eco Starter" not in self.badges:
            self.badges.append("Eco Starter")
        self.save()

# Fitness Tracker Models
class FitnessEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    weight = models.FloatField(default=0, help_text="Weight in kg")
    waist_size = models.FloatField(default=0, help_text="Waist size in cm")
    exercise_minutes = models.IntegerField(default=0, help_text="Exercise time in minutes")
    calories = models.IntegerField(default=0, help_text="Daily calorie intake")
    bmi = models.FloatField(default=0, help_text="Calculated BMI")

    def calculate_bmi(self, height_m):
        if height_m > 0:
            return self.weight / (height_m * height_m)
        return 0

    def save(self, *args, **kwargs):
        height_m = self.user.userprofile.height if hasattr(self.user, 'userprofile') else 1.7
        self.bmi = self.calculate_bmi(height_m)
        super().save(*args, **kwargs)

# Add height to UserProfile for BMI calculation
UserProfile.add_to_class('height', models.FloatField(default=1.7, help_text="Height in meters"))