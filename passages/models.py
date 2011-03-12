from django.db import models
from django.forms import ModelForm
from django.forms.widgets import SplitDateTimeWidget
from django.core import mail

from djangoappengine.utils import on_production_server

class CommonInfo(models.Model):
    '''
    The shared fields between both the classes need to be put in an
    abstract class. That way the non-relational DB won't get confused
    '''
    RUDDER_CHOICES = (
        ('S', 'Standard'),
        ('B', 'Becker'),
        ('Sc', 'Schottel type'),
        ('FT', 'Fishtail'),
        ('O', 'OTHER'),
    )
    ship_name     = models.CharField('Ship Name', max_length=100, blank=False)
    imo           = models.CharField('IMO', max_length=50, blank=False)
    dwt           = models.IntegerField('Summer DWT (t)', blank=False)  
    max_loa       = models.FloatField('LOA (m)', blank=False)
    max_beam      = models.FloatField('Beam (m)', blank=False)
    height        = models.FloatField('Mast Height (m)', blank=False)
    rudder        = models.CharField('Steering Type', max_length=2, choices=RUDDER_CHOICES, blank=False)
    
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
    speed         = models.FloatField('Speed (kts)', blank=True, null=True)
    bowthrust     = models.NullBooleanField('Operational Bowthrust', blank=False)
    radar         = models.IntegerField('Number of Radars', blank=True, null=True)
    email_address = models.EmailField('From (email)', blank=False)
    eta_breaksea  = models.DateTimeField('ETA Breaksea', blank=False)
    etd_sharpness = models.DateField('ETD Sharpness', blank=True, null=True)
    fwd_draft     = models.FloatField('Fwd FW Draft', blank=True, null=True)
    aft_draft     = models.FloatField('Aft FW Draft', blank=True, null=True)
    other         = models.CharField('Other Info', max_length=255, blank=True)
    dock_pilot    = models.NullBooleanField('Dock Pilot Required', blank=True)
    no_persons    = models.IntegerField('Total persons on board', blank=True, null=True)
    next_port     = models.CharField('Next Port', max_length=100, blank=True)
    date_added    = models.DateTimeField('Date Added', auto_now_add=True)
    
class PassageForm(ModelForm):
    class Meta:
        model = Passage
        widgets = {
            'eta_breaksea':  SplitDateTimeWidget(attrs={'class': 'dtField'},
                                                        date_format='%Y-%m-%d', time_format='%H:%M'),
                                                        }
    def sendAsEmail(self):
        '''
        This will form and send an email for this current form
        '''
        email = mail.EmailMessage()
        email.to = [ 'sam@z13.ath.cx', 'baytreecott@gmail.com' ]
        email.from_email = 'PreVisit <previsit@landing-lights.appspotmail.com>'
        email.subject = 'Pre-Visit Info Submission'
        t = 'The following has been submitted to the pre-visit form:\n\n'
        for i in sorted(self.data):
            t += (i + ':').ljust(20) + '\t' + self.data[i] + '\n'
        email.body = t
        if on_production_server:
            connection = mail.get_connection()
            connection.send_messages( [email] )
        
        
class VesselDetailForm(ModelForm):
    class Meta:
        model = VesselDetail
        
