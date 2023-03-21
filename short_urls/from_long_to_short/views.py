from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .models import *
from .forms import *

menu = [{'title': 'Homepage', 'url_name': 'home'},
        {'title': 'Feedback', 'url_name': 'feedback'},
        {'title': 'About me', 'url_name': 'about_me'}]

def index(request):
    form = NewShortURLForm(request.POST)
    full_url = ''
    subpart = ''
    short_url = ''
    if form.is_valid():
        full_url = form.cleaned_data.get('full_url')
        subpart = form.cleaned_data.get('subpart')
        try:
            if len(subpart) != 0:
                ShortURLs.objects.create(full_url=full_url, subpart = subpart, short_url='123' + subpart)
                print('Новая ссылка добавлена в Базу Данных.')
                return redirect('feedback')
            else:
                ShortURLs.objects.create(full_url=full_url,
                                         subpart='',
                                         short_url='123' + subpart)
                return redirect('about_me')
        except:
            form.add_error(None, 'This subpart already using, change it or leave the field empty')
            print('ДОЛЖНА БЫЛА ПОЯВИТСЬЯ ОШИБКА НА САЙТЕ', len(subpart))
        #form = NewShortURLForm
    all = ShortURLs.objects.all()
    context = {'form': form, 'all': all, 'menu': menu, 'title': 'Home page'}
    return render(request, 'from_long_to_short/index.html', context=context)

def about_me(request):
    context = {'menu': menu, 'title': 'About me'}
    return render(request, 'from_long_to_short/about_me.html', context=context)

def feedback(request):
    if request.method == 'POST':
        form = NewFeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = NewFeedbackForm()
    context = {'form': form, 'menu': menu, 'title': 'Feedback'}
    return render(request, 'from_long_to_short/feedback.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>This page was not found, sorry</h1>')