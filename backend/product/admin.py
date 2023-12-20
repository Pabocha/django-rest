from django.contrib import admin

# Register your models here.
from .models import *


class AdminProduct(admin.ModelAdmin):

    list_display = ['name', 'content', 'price']


admin.site.register(Product, AdminProduct)
