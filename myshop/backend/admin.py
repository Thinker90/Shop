from django.contrib import admin
from .models import User, Cart, CartItem


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "balance", "phone", "is_staff", "is_active")
    search_fields = ("username", "email", "phone")
    list_filter = ("is_staff", "is_active")
    ordering = ("username",)


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    readonly_fields = ("product", "quantity", "price_at_add", "total_price_display")

    def total_price_display(self, obj):
        return obj.total_price()
    total_price_display.short_description = "Итого"


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "created_at", "updated_at", "total_price_display")
    inlines = [CartItemInline]
    readonly_fields = ("created_at", "updated_at")

    def total_price_display(self, obj):
        return obj.total_price()
    total_price_display.short_description = "Сумма корзины"
