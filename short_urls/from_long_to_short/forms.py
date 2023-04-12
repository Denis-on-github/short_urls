from django import forms
from captcha.fields import CaptchaField
from django.core.exceptions import ValidationError
from django.shortcuts import redirect

from .models import *

class NewShortURLForm(forms.ModelForm):
    if settings.DEBUG is False:
        captcha = CaptchaField()

    class Meta:
        model = ShortURLs
        fields = ['full_url', 'subpart']
        widgets = {
            'full_url': forms.TextInput(attrs={'class': 'form-input'}),
            'subpart': forms.TextInput
        }

    def clean_full_url(self):
        data = self.cleaned_data['full_url']
        if not ShortURLs.objects.filter(full_url=data).exists():
            return data
        else:
            print('Валидатор сработал!')
            raise ValidationError(f'This URL is already short, please use it: {ShortURLs.objects.get(full_url=data).short_url}')

    def clean_subpart(self):
        data = self.cleaned_data['subpart']
        if ShortURLs.objects.filter(subpart=data).exists():
            raise ValidationError('This subpart is already used, please change it or left this field empty')
        elif 0 < len(data) < settings.LEN_SHORTS:
            raise ValidationError(f'Should be {settings.LEN_SHORTS} symbols in subpart')
        return data

class NewFeedbackForm(forms.Form):
    if settings.DEBUG is False:
        captcha = CaptchaField(label='Are you robot?')

    name = forms.CharField(max_length=50, label='Your name')
    email = forms.EmailField(label='Your e-mail')
    comment = forms.CharField(max_length=50,
                              label='Your feedback',
                              widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))