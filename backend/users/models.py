from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from phonenumber_field.modelfields import PhoneNumberField

#multiple choice answers 

TYPE_OF_TRAVELER_CHOICES = (
  ("Local People/ Work in Koh Tao", "Local People/ Work in Koh Tao"),
  ("Tourist", "Tourist")
)

TYPE_OF_ARRIVING_BOAT_CHOICES = (
  ("Lomprayah Boat Samui/Surat", "Lomprayah Boat Samui/Surat"),
  ("Lomprayah Boat Chumpon", "Lomprayah Boat Chumphon"),
  ("Night Boat SURATTHANI", "Night Boat SURATTHANI"),
  ("Night Boat CHUMPHON", "Night Boat CHUMPHON"),
  ("Private Speedboat", "Private Speedboat"),
  ("Other", "Other")
)

YES_NO_CHOICES = (
  ("Yes", "Yes"),
  ("No", "No")
)

# User Profile that includes  traveler info, arrival info and contact info
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  first_name = models.CharField(max_length=25, default='', blank=True)
  last_name = models.CharField(max_length=25, default='', blank=True)
  age = models.IntegerField(default=None, null=True)
  nationality = models.CharField(max_length=25, default='', blank=True)
  passport_num = models.CharField(max_length=25, default='', blank=True)
  travel_from = models.CharField(max_length=100, default='', blank=True)
  date_of_arrival = models.DateField(default=None, null=True)
  accommodation = models.CharField(max_length=100, default='', blank=True)
  phone_number = PhoneNumberField(default=None, null=True)

  type_of_traveler = MultiSelectField(choices=TYPE_OF_TRAVELER_CHOICES)
  type_of_arriving_boat = MultiSelectField(choices=TYPE_OF_ARRIVING_BOAT_CHOICES)
  restricted_area = MultiSelectField(choices=YES_NO_CHOICES)

  is_complete = models.BooleanField(default=False)
