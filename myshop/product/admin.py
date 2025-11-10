from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "stock", "rating")
    list_filter = ("category",)
    search_fields = ("name", "description")
    list_editable = ("price", "stock", "rating")
    ordering = ("-rating",)