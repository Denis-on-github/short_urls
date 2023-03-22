from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .models import *
from .forms import *

import random

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
        if ShortURLs.objects.get(full_url=full_url):
            form.add_error('full_url', f'We short this URL previously! Use this: http://127.0.0.1:8000/{ShortURLs.objects.get(full_url=full_url)}/')
        else:
            if len(subpart) == 0:
                subpart = ''.join(random.choices(settings.SYMBOLS, k=settings.LEN_SHORTS))
                ShortURLs.objects.create(full_url=full_url,
                                        subpart=subpart,
                                        short_url='123' + subpart)
                return f'Your short link: http://127.0.0.1:8000/{ShortURLs.objects.get(full_url=full_url)}'

        # elif ShortURLs.objects.get(subpart=subpart):
        #     form.add_error('subpart', 'This subpart used, try another one or leave it empty.')
        # else:
        #     subpart = ''.join(random.choices(settings.SYMBOLS, k=settings.LEN_SHORTS))
        #     ShortURLs.objects.create(full_url=full_url,
        #                             subpart=subpart,
        #                             short_url='123' + subpart)
        #     return redirect('feedback')
            # try:
            #     ShortURLs.objects.create(full_url=full_url, subpart = subpart, short_url='123' + subpart)
            #     return redirect('feedback')
            # except:
            #     # как сделать вывод конкретной ошибки к нужному полю, потому что сейчас, высвечиваются обе
            #     # ошибки, независимо от того, в каком поле идет повтор
            #     form.add_error('full_url', 'We short this URL previously!')
            #     form.add_error('subpart', 'This subpart already using, change it or leave the field empty')
    else:
        form = NewShortURLForm()
        # try:
        #     if len(subpart) != 0:
        #         ShortURLs.objects.create(full_url=full_url, subpart = subpart, short_url='123' + subpart)
        #         print('Новая ссылка добавлена в Базу Данных.')
        #         return redirect('feedback')
        #     else:
        #         ShortURLs.objects.create(full_url=full_url,
        #                                  subpart='',
        #                                  short_url='123' + subpart)
        #         return redirect('about_me')
        # except:
        #     form.add_error(None, 'This subpart already using, change it or leave the field empty')
        #     print('ДОЛЖНА БЫЛА ПОЯВИТСЬЯ ОШИБКА НА САЙТЕ', len(subpart))
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