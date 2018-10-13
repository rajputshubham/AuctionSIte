from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    location = models.CharField(max_length=100)
    user_image = models.ImageField(upload_to='profile_image', blank=True)

# class AbstractUser(models.Model):
#     username = models.CharField(max_length=50)
#     user_email = models.EmailField(max_length=70, blank=True)
#     password = models.CharField(max_length=50)
#     location = models.CharField(max_length=100)
#     user_image = models.ImageField(upload_to='profile_image', blank=True)
#     User.objects.create_user(username, user_email, password)


class Product(models.Model):
    seller_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    product_desc = models.CharField(max_length=1000)
    creation_time = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    base_price = models.IntegerField()
    product_image = models.ImageField(upload_to='product_images')


class Bid(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    bidder_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    bid_time = models.DateTimeField(auto_now_add=True)
    bid_price = models.IntegerField()
    is_winning = models.BooleanField(default=False)
