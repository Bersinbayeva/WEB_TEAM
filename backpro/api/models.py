from django.db import models
from django.contrib.auth.models import User


class CategoryManager(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)


class Category(models.Model):
    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    # objects = CategoryManager()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Sections(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="section_c",blank=True, null=True)

    class Meta:
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Product(models.Model):
    # img = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=50)
    sections = models.ForeignKey(Sections, on_delete=models.CASCADE, related_name="product", blank=True, null=True)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'status': self.status,
        }

class Basket(models.Model):
    product = models.ManyToManyField(Product)
    count = models.IntegerField()

    def __str__(self):
        return '{}: {}'.format(self.count)

    def to_json(self):
        return {
            'count': self.count,
        }