from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'product_category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ('-id',)

    def __str__(self):
        return self.name

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_id =models.CharField(max_length=100)
    category =models.ManyToManyField(Category, blank=True)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    actual_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=10, decimal_places=2)
    rating_count = models.IntegerField(default=1)
    about_product = models.TextField()
    user_id = models.CharField(max_length=100)
    user_name= models.CharField(max_length=100)
    review_id = models.CharField(max_length=100)
    review_title = models.CharField(max_length=100)
    review_content = models.CharField(max_length=100)
    img_link = models.CharField(max_length=100)
    product_link =models.CharField(max_length=100)


    class Meta:
        db_table = 'product_product'
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ('-id',)

    def __str__(self):
        return self.product_name