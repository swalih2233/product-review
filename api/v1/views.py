import requests
import datetime
from django.db.models import Sum

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny

from django.shortcuts import get_object_or_404

from .serializers import ProductSerializer, CategorySerializer

from product.models import Product, Category


@api_view(["GET"])
@permission_classes ([AllowAny])
def product_details(request,id):
    instance = get_object_or_404(Product, product_id=id)
  
    
    context ={
        "request":request
    }
    serializer = ProductSerializer(instance,context=context)


    response_data ={
        "status_code":6000,
        "data":serializer.data
    }
    return Response(response_data) 


@api_view(["GET"])
@permission_classes ([AllowAny])
def list_products(request):
    instances = Product.objects.all().order_by('-rating')[:5]

    context = {
        "request": request
    }

    serializer = ProductSerializer(instances, many=True, context=context)

    response_data = {
        "status_code": 6000,
        "data": serializer.data,
    }

    return Response(response_data)


@api_view(["GET"])
@permission_classes ([AllowAny])
def discount_category(request):
    category = request.GET.get('category')
    category = Category.objects.get(name__icontains=category)
    instances = Product.objects.filter(category=category)

    instances_count =instances.count()

    total_discount_percentage = instances.aggregate(Sum("discount_percentage"))["discount_percentage__sum"]

    average = total_discount_percentage / instances_count

    response_data ={
        "status_code":6000,
        "average_dis": average
    }
    return Response(response_data) 



@api_view(["GET"])
@permission_classes ([AllowAny])
def search_product(request):
    instances = Product.objects.all()
    category = request.GET.get('category')
    product_name = request.GET.get('product_name')
    rating = request.GET.get('rating')
    price = request.GET.get('price')

    if category:
        category = Category.objects.get(name__icontains=category)
        instances = instances.filter(category=category)

    if product_name:
        instances = instances.filter(name__icontains=product_name)

    if rating:
        instances = instances.filter(rating__gte=rating)

    if price:
        instances = instances.filter(price__lte=price)


    context ={
        "request":request
    }
    serializer = ProductSerializer(instances,context=context)


    response_data ={
        "status_code":6000,
        "data":serializer.data
    }
    return Response(response_data) 
