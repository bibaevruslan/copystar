from django.db import models


class CountriesOfOrigin(models.Model):
    title = models.CharField(max_length=100, null=False)


class ProductModel(models.Model):
    title = models.CharField(max_length=100)


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=1000000, decimal_places=2)
    category = models.CharField(max_length=100)
    image_id = models.CharField(max_length=100)
    year_of_production = models.DateField()
    country_of_origin_id = models.ForeignKey(CountriesOfOrigin, on_delete=models.CASCADE)
    product_model_id = models.ForeignKey(ProductModel, on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=100, null=False)


class Order(models.Model):
    status = models.CharField(max_length=100, null=False)
    timestamp = models.DateTimeField(auto_now_add=True, null=False)
    dataset_id = models.IntegerField(null=False)
