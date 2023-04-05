# Generated by Django 4.2 on 2023-04-04 00:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design_title', models.CharField(max_length=255)),
                ('province', models.CharField(choices=[('AB', 'Alberta'), ('BC', 'British Columbia'), ('MB', 'Manitoba'), ('NB', 'New Brunswick'), ('NL', 'Newfoundland and Labrador'), ('NT', 'Northwest Terrirories'), ('NS', 'Nova Scotia'), ('ON', 'Ontario'), ('PE', 'Prince Edward Island'), ('QC', 'Quebec'), ('SK', 'Saskatchewan'), ('YT', 'Yukon')], max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('description', models.TextField(max_length=500)),
                ('design_photo_1', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('design_photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('design_photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('design_photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('design_photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('features', models.CharField(choices=[('Home theatre system', 'Home theatre system'), ('Wooden Floor', 'Wooden Floore'), ('Unbreakable glasses', 'Unbreakable glasses'), ('Air Conditioning', 'Air Conditioning'), ('Heating', 'Heating'), ('Alarm System', 'Alarm System'), ('ParkingGarage', 'ParkingGarage'), ('Solar Powered', 'Solar Powered'), ('Sensor Lights', 'Sensor Lights'), ('Camera System', 'Camera System'), ('Furnished', 'Furnished'), ('Non-Furnished', 'Non-Furnished'), ('Greenhouse', 'Greenhouse')], max_length=100)),
                ('Exterior_wall_construction', models.CharField(max_length=300)),
                ('interior', models.CharField(max_length=100)),
                ('is_featured', models.BooleanField(max_length=100)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]