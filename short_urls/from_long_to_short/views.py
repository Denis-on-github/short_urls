from django.http import HttpResponseNotFound, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, FormView
from .models import *
from .forms import *
import redis
import random


redis_instance = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)

menu = [{'title': 'About me', 'url_name': 'about_me'},
        {'title': 'Feedback', 'url_name': 'feedback'},
]

def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

        # if redis_instance.exists(ip_client) == 0:
        #     redis_instance.set(ip_client, 'None')
        #     redis_instance.expire(ip_client, settings.SESSION_TIME_LIMIT)
        #     print('Иф сработал, запись в БД создана. Она будет удалена через:', settings.SESSION_TIME_LIMIT, 'секунд')
        #     return redirect('home')
        # else:
        #     print('Элс сработал, запись уже создана в БД!')
        #     return redirect('home')

class HomePage(CreateView, ListView):
    form_class = NewShortURLForm
    model = ShortURLs
    template_name = 'from_long_to_short/index.html'
    context_object_name = 'all_shorts'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        self.object_list = self.get_queryset()
        context = super().get_context_data(**kwargs)
        context['title'] = 'Homepage'
        context['menu'] = menu
        return context

    def get_queryset(self):
        ip_client = get_ip(self.request)
        return ShortURLs.objects.filter(user__user_ip=ip_client)

    def form_valid(self, form):
        full_url = form.cleaned_data['full_url']
        subpart = form.cleaned_data['subpart']
        ip_client = get_ip(self.request)

        if len(subpart) == 0:
            subpart = ''.join(random.choices(settings.SYMBOLS, k=settings.LEN_SHORTS))
            short_url = 'http://127.0.0.1:8000/' + subpart + '/'
            if Users.objects.filter(user_ip=ip_client).exists():
                ShortURLs.objects.create(full_url=full_url,
                                         subpart=subpart,
                                         short_url=short_url,
                                         user=Users.objects.get(user_ip=ip_client))
                redis_instance.expire(ip_client, settings.SESSION_TIME_LIMIT)
            else:
                Users.objects.create(user_ip=ip_client)
                redis_instance.set(ip_client, 'None')
                redis_instance.expire(ip_client, settings.SESSION_TIME_LIMIT)
                ShortURLs.objects.create(full_url=full_url,
                                         subpart=subpart,
                                         short_url=short_url,
                                         user=Users.objects.get(user_ip=ip_client))
        else:
            short_url = 'http://127.0.0.1:8000/' + subpart + '/'
            if Users.objects.filter(user_ip=ip_client).exists():
                ShortURLs.objects.create(full_url=full_url,
                                         subpart=subpart,
                                         short_url=short_url,
                                         user=Users.objects.get(user_ip=ip_client))
                redis_instance.expire(ip_client, settings.SESSION_TIME_LIMIT)
            else:
                Users.objects.create(user_ip=ip_client)
                redis_instance.set(ip_client, 'None')
                redis_instance.expire(ip_client, settings.SESSION_TIME_LIMIT)
                ShortURLs.objects.create(full_url=full_url,
                                         subpart=subpart,
                                         short_url=short_url,
                                         user=Users.objects.get(user_ip=ip_client))

        # if redis_instance.type(ip_client) == b'string':
        #     short_url = 'http://127.0.0.1:8000/' + subpart + '/'
        #     redis_instance.delete(ip_client)
        #     redis_instance.hmset(ip_client, {short_url: full_url})
        #     redis_instance.expire(ip_client, settings.SESSION_TIME_LIMIT)
        # else:
        #     short_url = 'http://127.0.0.1:8000/' + subpart + '/'
        #     redis_instance.hmset(ip_client, {short_url: full_url})
        #     redis_instance.expire(ip_client, settings.SESSION_TIME_LIMIT)
        return redirect('home')

def about_me(request):
    context = {'menu': menu, 'title': 'About me'}
    return render(request, 'from_long_to_short/about_me.html', context=context)

class Feedback(FormView):
    form_class = NewFeedbackForm
    template_name = 'from_long_to_short/feedback.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Feedback'
        return context

    def form_valid(self, form):
        return redirect('home')

# def feedback(request):
#     if request.method == 'POST':
#         form = NewFeedbackForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#     else:
#         form = NewFeedbackForm()
#     context = {'form': form, 'menu': menu, 'title': 'Feedback'}
#     return render(request, 'from_long_to_short/feedback.html', context=context)

def get_full_url(subpart: str) ->  str:
    try:
        short_url = ShortURLs.objects.get(subpart=subpart)
    except:
        raise KeyError("Sorry, but we don't know where you go, try another short or generate new one")
    short_url.request_count += 1
    short_url.save()
    return short_url.full_url

def redirected(request, subpart):
    try:
        full_url = get_full_url(subpart)
        return redirect(full_url)
    except:
        return HttpResponseNotFound("Sorry, but we don't know where you go, try another short or generate new one")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>This page was not found, sorry</h1>')