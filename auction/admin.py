from django.contrib import admin
from auction.models import User, Product, Bid
# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Bid)