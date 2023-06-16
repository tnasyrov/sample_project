from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()


class Order(models.Model):
    datetime = models.DateTimeField()


class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.PositiveSmallIntegerField()
    prod_id = models.UUIDField()
    description = models.TextField()



products_courses = Product.objects.filter(name__contains='Курс')
products_lt_2500 = Product.objects.filter(price__lt=2500)
products_starts_with_course = Product.objects.filter(name__istartswith='курс')