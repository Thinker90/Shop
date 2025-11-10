from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from backend.models import Cart

# Главная страница
def index(request):
    categories = Category.objects.all()
    products = Product.objects.order_by('-rating')[:12]  # последние 12 товаров по рейтингу
    return render(request, 'index.html', {
        'categories': categories,
        'products': products
    })

# Страница категории с товарами
def category_detail(request, category_id):
    categories = Category.objects.all()
    category = get_object_or_404(Category, id=category_id)
    return render(request, 'categories.html', {
        'categories': categories,
        'category': category,
        'products': category.products.all()
    })

# Страница конкретного товара
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    categories = Category.objects.all()
    return render(request, 'product_detail.html', {
        'product': product,
        'categories': categories
    })

# Добавление товара в корзину (упрощённо)
def add_to_cart(request, product_id):
    if not request.user.is_authenticated:
        return redirect('login')
    product = get_object_or_404(Product, id=product_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    from backend.models import CartItem
    # Добавляем товар или увеличиваем количество
    item, created = CartItem.objects.get_or_create(cart=cart, product=product, defaults={'quantity': 1, 'price_at_add': product.price})
    if not created:
        item.quantity += 1
        item.save()
    return redirect('product_detail', product_id=product.id)
