from unicodedata import category
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import redirect
from django.urls import reverse
from GlaCine.forms import CategoryForm, PageForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime
from .models import *

def jump_page(request):

    return redirect(reverse('GlaCine:index', kwargs={'page': 0}))
def index(request,page):
    cinema_num_per_page = 8

    cinemas = list(Cinema.objects.all())
    cinema_sum = Cinema.objects.count()
    page_max = (cinema_sum-1)//cinema_num_per_page+1
    
    def get_visit(c):
        return c.visit

    cinemas.sort(key=get_visit, reverse=True)
    cinemas= cinemas[page*cinema_num_per_page:(page+1)*cinema_num_per_page]
    context = {
        'cinemas':cinemas,
        'pages':range(page_max),
        'page_num':page,
    }
    return render(request,"GlaCine/index.html", context)

def cinema(request, cinema_name):

    response= render(request,f'GlaCine/{cinema_name}.html')
    return response

def review(request):
    context = {
    }
    return render(request,"GlaCine/review.html", context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('GlaCine:index'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print("Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'GlaCine/login.html')

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    return render(request, 'GlaCine/register.html',
                  context={'user_form': user_form, 
                           'profile_form': profile_form, 
                           'registered': registered})