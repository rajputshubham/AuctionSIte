from django.contrib import admin
from auction.models import CustomUser, Product, Bid
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Product)
admin.site.register(Bid)