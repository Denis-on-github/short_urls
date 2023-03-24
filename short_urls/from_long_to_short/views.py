from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, FormView
from .models import *
from .forms import *

import random

menu = [{'title': 'About me', 'url_name': 'about_me'},
        {'title': 'Feedback', 'url_name': 'feedback'}
]

class HomePage(CreateView, ListView):
    form_class = NewShortURLForm
    model = ShortURLs
    template_name = 'from_long_to_short/index.html'
    context_object_name = 'all_shorts'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Homepage'
        context['menu'] = menu
        return context

    def form_valid(self, form):
        full_url = form.cleaned_data.get('full_url')
        subpart = form.cleaned_data.get('subpart')
        '''
        В данный момент мы сокращаем ссылку и заносим в нашу БД,
        БЕЗ проверок на то, есть ли у нас в БД такая ссылка или ее шорт часть!
        '''
        if len(subpart) != 0:
            ShortURLs.objects.create(full_url=full_url,
                                     subpart=subpart,
                                     short_url='http://127.0.0.1:8000/' + subpart + '/')
        else:
            subpart = ''.join(random.choices(settings.SYMBOLS, k=settings.LEN_SHORTS))
            ShortURLs.objects.create(full_url=full_url,
                                     subpart=subpart,
                                     short_url='http://127.0.0.1:8000/' + subpart + '/')
        return redirect('feedback')

def about_me(request):
    context = {'menu': menu, 'title': 'About me'}
    return render(request, 'from_long_to_short/about_me.html', context=context)

class Feedback(FormView):
    form_class = NewFeedbackForm
    template_name = 'from_long_to_short/feedback.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        return redirect('home')

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