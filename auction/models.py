from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    user_image = models.ImageField(upload_to='profile_image', blank=True)


class Products(models.Model):
    seller_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    product_desc = models.CharField(max_length=1000)
    creation_time = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    base_price = models.IntegerField()
    product_image = models.ImageField(upload_to='product_images')


class Bids(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    bidder_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    bid_time = models.DateTimeField(auto_now_add=True)
    bid_price = models.IntegerField()
    winning_bid = models.IntegerField()
