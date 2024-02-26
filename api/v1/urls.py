from django.urls import path
from api.v1 import views



app_name = "api"
 
urlpatterns = [
  
  path("product_details/<int:id>/", views.product_details),

  path("list_top_rated_products/", views.list_products),

  path("average_discount_category/<int:id>/", views.discount_category),

  path("search_product/", views.search_product),

  

]
