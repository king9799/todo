from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=256)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)
    name = models.CharField(max_length=64)
    price = models.IntegerField(default=0)
    pr_data = models.DateField(auto_now_add=True)
    amount = models.IntegerField(default=0)
    desc = models.TextField()

    def __str__(self):
        return self.name
