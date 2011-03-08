from django.db import models
from django.forms import ModelForm

class CommonInfo(models.Model):
    '''
    The shared fields between both the classes need to be put in an
    abstract class. That way the non-relational DB won't get confused
    '''
    RUDDER_CHOICES = (
        ('S', 'Standard'),
        ('B', 'Becker'),
        ('Sc', 'Schottel'),
        ('FT', 'Fishtail'),
        ('O', 'OTHER'),
    )
    ship_name = models.CharField('Ship Name', max_length=100)
    imo = models.CharField('IMO', max_length=50)
    dwt = models.IntegerField('Summer DWT (t)', blank=True, null=True)  
    max_loa = models.FloatField('LOA (m)', blank=True, null=True)
    max_beam = models.FloatField('Beam (m)', blank=True, null=True)
    speed = models.FloatField('Speed (kts)', blank=True, null=True)
    height = models.FloatField('Maximum height of mast above keel (m)', blank=True, null=True)
    rudder = models.CharField('Steering Type', max_length=2, choices=RUDDER_CHOICES, blank=True)
    bowthrust = models.BooleanField('Operational Bowthrust', blank=True, null=True)
    radar = models.IntegerField('Number of Radars', blank=True, null=True)
    email_address = models.EmailField('From (email)', blank=True)
    class Meta:
        abstract = True
    
class VesselDetail(CommonInfo):
    '''
    This class contains the details of vessels that are less likely
    to change. In the datastore each unique ship_name will have an
    entry in this table, with the most recent details from the
    Passage table.
    '''
    

class Passage(CommonInfo):
    '''
    The Passage model subclasses the VesselDetail model since it requires most
    of the same fields. A new entry will be created in the datastore for each
    new Passage. There are *no* clever relationships with the VesselDetail model.
    '''
    eta_breaksea = models.DateTimeField('ETA Breaksea', blank=True, null=True)
    etd_sharpness = models.DateTimeField('ETD Sharpness', blank=True, null=True)
    fwd_draft = models.FloatField('Fwd FW Draft', blank=True, null=True)
    aft_draft = models.FloatField('Aft FW Draft', blank=True, null=True)
    other = models.CharField('Other Info', max_length=255, blank=True)
    dock_pilot = models.BooleanField('Dock Pilot Required', blank=True, null=True)
    no_persons = models.IntegerField('Total persons on board', blank=True, null=True)
    next_port = models.CharField('Next Port', max_length=100, blank=True)
    date_added = models.DateTimeField('Date Added', auto_now_add=True)
    
class PassageForm(ModelForm):
    class Meta:
        model = Passage
        
        
