from django.contrib import admin
from .models import *
# Register your models here.
#
# admin.site.register(Products)
admin.site.register(Category)


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'amount', 'desc']
    list_filter = ('name', 'category')
    search_fields = ('name', 'desc')
    raw_id_fields = ('category',)