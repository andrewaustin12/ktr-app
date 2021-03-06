# Generated by Django 3.2 on 2021-04-20 23:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, default='', max_length=25)),
                ('last_name', models.CharField(blank=True, default='', max_length=25)),
                ('age', models.IntegerField(default=None, null=True)),
                ('nationality', models.CharField(blank=True, default='', max_length=25)),
                ('passport_num', models.CharField(blank=True, default='', max_length=25)),
                ('travel_from', models.CharField(blank=True, default='', max_length=100)),
                ('date_of_arrival', models.DateField(default=None, null=True)),
                ('accommodation', models.CharField(blank=True, default='', max_length=100)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(default=None, max_length=128, null=True, region=None)),
                ('type_of_traveler', multiselectfield.db.fields.MultiSelectField(choices=[('Local People/ Work in Koh Tao', 'Local People/ Work in Koh Tao'), ('Tourist', 'Tourist')], max_length=37)),
                ('type_of_arriving_boat', multiselectfield.db.fields.MultiSelectField(choices=[('Lomprayah Boat Samui/Surat', 'Lomprayah Boat Samui/Surat'), ('Lomprayah Boat Chumpon', 'Lomprayah Boat Chumphon'), ('Night Boat SURATTHANI', 'Night Boat SURATTHANI'), ('Night Boat CHUMPHON', 'Night Boat CHUMPHON'), ('Private Speedboat', 'Private Speedboat'), ('Other', 'Other')], max_length=115)),
                ('restricted_area', multiselectfield.db.fields.MultiSelectField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=6)),
                ('is_complete', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
