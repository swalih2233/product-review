from rest_framework import serializers
from product.models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('product_name', 'product_id', 'category' , 'discounted_price', 'actual_price', 'discount_percentage', 'rating', 'rating_count', 'about_product', 'user_id' ,'user_name' ,'review_id', 'review_title', 'review_content', 'img_link', 'product_link')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name')