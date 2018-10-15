from django.contrib import admin
from auction.models import AbstractUser, Product, Bid
# Register your models here.
admin.site.register(AbstractUser)
admin.site.register(Product)
admin.site.register(Bid)