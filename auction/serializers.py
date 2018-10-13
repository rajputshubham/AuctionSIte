from rest_framework import serializers
from auction.models import AbstractUser, Product, Bid


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = AbstractUser
        fields = ['username', 'email', 'location']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['seller_id', 'product_name', 'product_desc', 'creation_time', 'start_time', 'end_time', 'base_price']


class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = ['product_id', 'bidder_id', 'bid_time', 'bid_price', 'is_winning']
