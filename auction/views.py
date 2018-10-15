from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.db import models

from auction.forms import SignUpForm, ProductForm


@login_required
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.abstractuser.username = form.cleaned_data.get('username')
            user.abstractuser.location = form.cleaned_data.get('location')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('productsignup')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required()
def productsignup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.abstractuser.seller_id = request.user.id
            user.abstractuser.product_name = form.cleaned_data.get('product_name')
            user.abstractuser.product_desc = form.cleaned_data.get('product_desc')
            user.abstractuser.creation_time = models.DateTimeField(auto_now_add=True)
            user.abstractuser.start_time = form.cleaned_data.get('start_time')
            user.abstractuser.end_time = form.cleaned_data.get('end_time')
            user.abstractuser.base_price = form.cleaned_data.get('base_price')
            user.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'productsignup.html', {'form': form})