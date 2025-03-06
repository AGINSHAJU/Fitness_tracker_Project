# Generated by Django 5.0 on 2025-03-05 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_remove_carbonentry_diet_meals_carbonentry_beef_meals_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='carbonentry',
            name='end_lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='carbonentry',
            name='end_lng',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='carbonentry',
            name='start_lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='carbonentry',
            name='start_lng',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
