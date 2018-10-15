from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from auction.models import Product


class SignUpForm(UserCreationForm):
    location = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'location', 'password1', 'password2', )


class ProductForm(forms.Form):
    product_name = forms.CharField(max_length=200)
    product_desc = forms.CharField(max_length=1000)
    start_time = forms.DateTimeField()
    end_time = forms.DateTimeField()
    base_price = forms.IntegerField()

    class Meta:
        model = Product
        fields = ('product_name', 'product_desc', 'start_time', 'end_time', 'base_price', )