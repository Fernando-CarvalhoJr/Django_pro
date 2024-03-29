from django import forms
from models import *

class AddForm(forms.Form):
    
    class Meta:
        model = models.Contact
        fields = ('name', 'relation', 'phone', 'email',)