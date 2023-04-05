from datetime import datetime
from django.db import models
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

# Create your models here.
class Design(models.Model):
    
    province_choice =(
        ('AB', 'Alberta'),
        ('BC', 'British Columbia'),
        ('MB', 'Manitoba'),
        ('NB', 'New Brunswick'),
        ('NL', 'Newfoundland and Labrador'),
        ('NT', 'Northwest Terrirories'), 
        ('NS', 'Nova Scotia'),
        ('ON', 'Ontario'),
        ('PE', 'Prince Edward Island'),
        ('QC', 'Quebec'),
        ('SK', 'Saskatchewan'),
        ('YT', 'Yukon'),   
    )
    features_choices = (
        ('Home theatre system', 'Home theatre system'),
        ('Wooden Floor', 'Wooden Floore'),
        ('Unbreakable glasses', 'Unbreakable glasses'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Heating', 'Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkingGarage', 'ParkingGarage'),
        ('Solar Powered', 'Solar Powered'),
        ('Sensor Lights', 'Sensor Lights'),
        ('Camera System', 'Camera System'),
        ('Furnished', 'Furnished'),
        ('Non-Furnished', 'Non-Furnished'),
        ('Greenhouse', 'Greenhouse'),
    )
    
    floors_choices = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
    )
    
    design_title = models.CharField(max_length=255)
    province = models.CharField(choices=province_choice, max_length=100,)
    city = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.IntegerField()
    description = RichTextField()
    design_photo = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    design_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    design_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    design_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    design_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    design_photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    features = MultiSelectField(choices=features_choices)
    Exterior_wall_construction = models.CharField(max_length=300)
    interior = models.CharField(max_length=100)
    squarefeet = models.IntegerField()
    floors =  models.CharField(choices=floors_choices, max_length=10, blank=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    
    
    def __str__(self):
        return self.design_title