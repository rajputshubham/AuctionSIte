from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class AbstractUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, default='')
    location = models.CharField(max_length=100)
    user_image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        AbstractUser.objects.create(user=instance)
    instance.abstractuser.save()

class Product(models.Model):
    seller_id = models.ForeignKey(AbstractUser, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    product_desc = models.CharField(max_length=1000)
    creation_time = models.DateTimeField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    base_price = models.IntegerField()
    product_image = models.ImageField(upload_to='product_images', blank=True)

@receiver(post_save, sender=AbstractUser)
def update_product_profile(sender, instance, created, **kwargs):
    if created:
        Product.objects.create(user=instance)
    instance.product.save()


class Bid(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    bidder_id = models.ForeignKey(AbstractUser, on_delete=models.CASCADE)
    bid_time = models.DateTimeField(auto_now_add=True)
    bid_price = models.IntegerField()
    is_winning = models.BooleanField(default=False)
