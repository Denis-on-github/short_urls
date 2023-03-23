from django import forms
from django.core.exceptions import ValidationError

from .models import *

class NewShortURLForm(forms.ModelForm):
    class Meta:
        model = ShortURLs
        fields = ['full_url', 'subpart']
        widgets = {
            'full_url': forms.TextInput(attrs={'class': 'form-input'}),
            'subpart': forms.TextInput
        }

    # def clean_full_url(self):
    #     full_url = self.cleaned_data['full_url']
    #     if ShortURLs.objects.get(full_url=full_url):
    #         raise ValidationError('We short this URL previously!')
    #     return full_url

    # def clean_subpart(self):
    #     subpart = self.cleaned_data['subpart']
    #     if ShortURLs.objects.filter(subpart=subpart):
    #         raise ValidationError('This subpart already using, change it or leave the field empty')
    #     return subpart

class NewFeedbackForm(forms.Form):
    name = forms.CharField(max_length=50, label='Your name')
    comment = forms.CharField(max_length=50, label='Your feedback')