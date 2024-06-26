# Generated by Django 4.2.1 on 2024-06-26 11:29

from django.db import migrations, models
from django.core.exceptions import ObjectDoesNotExist

all_vehicles = [
    # Bocken last values as per 26/06/24: 37684	37697
    {"vehicle_type" : "Bocken", "vehicle_meter_start": 37684, "vehicle_meter_stop": 37697},
    {"vehicle_type" : "Bjällran", "vehicle_meter_start": 0, "vehicle_meter_stop": 0}
]

def add_default_vehicles(apps, schema_editor):
    model = apps.get_model("bocken", "Vehicle")
    for vehicle in all_vehicles:
            created_vehicle = model.objects.create(
                vehicle_type=vehicle['vehicle_type'],
                vehicle_meter_start = vehicle['vehicle_meter_start'],
                vehicle_meter_stop = vehicle['vehicle_meter_stop'],
            )


def remove_default_vehicles(apps, schema_editor):
    model = apps.get_model("bocken", "Vehicle")
    for vehicle in all_vehicles:
        try:
            vehicle_to_delete = model.objects.get(vehicle_type=vehicle['vehicle_type']).delete()
        except ObjectDoesNotExist:
            continue

class Migration(migrations.Migration):

    dependencies = [
        ('bocken', '0004_alter_t_numbers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_type', models.CharField(max_length=60, verbose_name='Type')),
                ('vehicle_meter_start',models.PositiveIntegerField(default=0,verbose_name='Meter at start')),
                ('vehicle_meter_stop',models.PositiveIntegerField(default=0,verbose_name='Meter at stop')),
            ],
            options={
                'verbose_name': 'Vehicle type',
                'verbose_name_plural': 'Vehicle types',
            },
        ),
        migrations.RunPython(add_default_vehicles, remove_default_vehicles)
    ]
