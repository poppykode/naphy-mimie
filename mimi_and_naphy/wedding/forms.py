from django import forms
from django.utils.translation import gettext_lazy as _
from .models import (
    RSVP,Contact
)

class RSVPForm(forms.ModelForm):
    class Meta:
        model = RSVP
        fields = ('name','number_of_attendees', 'phone_number','holy_metromony','wedding_party','message')
        labels = {
            'holy_metromony': _('Holy Matrimony'),
            'wedding_party':_('Wedding Party'),
        }
        widgets = {
            'message': forms.Textarea(attrs={'cols': 80, 'rows': 5}),  
        }

class  ContaUsForm(forms.ModelForm):

    class Meta:
        model = Contact 
        fields =('name','email','phone','message',)  
        labels = {
            'phone':_('Phone Number'),
        }
        widgets = {
            'message': forms.Textarea(attrs={'cols': 80, 'rows': 5}),  
        }   
