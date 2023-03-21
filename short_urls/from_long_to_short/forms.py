from django import forms
from .models import *

class NewShortURLForm(forms.Form):
    full_url = forms.URLField(label='Full URL')
    subpart = forms.CharField(max_length=settings.LEN_SHORTS, min_length=settings.LEN_SHORTS, required=False)

class NewFeedbackForm(forms.Form):
    name = forms.CharField(max_length=50, label='Your name')
    comment = forms.CharField(max_length=50, label='Your feedback')