from django.contrib import admin
from .models import Category
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    display = ('id', 'name', 'exp')
    search_fields = ('name')

    admin.site.register(Category)