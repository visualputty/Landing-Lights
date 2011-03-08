from django.db import models
from django.forms import ModelForm

# Create your models here.
class Passage(models.Model):
    RUDDER_CHOICES = (
        ('S', 'Standard'),
        ('B', 'Becker'),
        ('Sc', 'Schottel'),
        ('FT', 'Fishtail'),
        ('O', 'OTHER'),
    )
    ship_name = models.CharField('Ship Name', max_length=100)
    imo = models.CharField('IMO', max_length=50)
    eta_breaksea = models.DateTimeField('ETA Breaksea', null=True)
    etd_sharpness = models.DateTimeField('ETD Sharpness', null=True)
    max_loa = models.FloatField('LOA (m)', null=True)
    max_beam = models.FloatField('Beam (m)', null=True)
    fwd_draft = models.FloatField('Fwd FW Draft', null=True)
    aft_draft = models.FloatField('Aft FW Draft', null=True)
    dwt = models.IntegerField('Summer DWT (t)', null=True)  
    speed = models.FloatField('Speed (kts)', null=True)
    height = models.FloatField('Maximum height of mast above keel (m)', null=True)
    rudder = models.CharField('Steering Type', max_length=2, choices=RUDDER_CHOICES)
    bowthrust = models.BooleanField('Operational Bowthrust', null=True)
    radar = models.IntegerField('Number of Radars', null=True)
    other = models.CharField('Other Info', max_length=255)
    dock_pilot = models.BooleanField('Dock Pilot Required', null=True)
    no_persons = models.IntegerField('Total persons on board', null=True)
    next_port = models.CharField('Next Port', max_length=100)
    email_address = models.EmailField('From (email)')
    date_added = models.DateTimeField('Date Added', auto_now_add=True)
    
class PassageForm(ModelForm):
    class Meta:
        model = Passage