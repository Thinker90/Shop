from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from product import views as product_views
from backend import views as backend_views
from django.contrib.auth import views as auth_views

# Авторизация
login_view = auth_views.LoginView.as_view(template_name='login.html')
logout_view = auth_views.LogoutView.as_view(next_page='index')  # убрали allow_get

urlpatterns = [
    path('admin/', admin.site.urls),

    # Главная
    path('', product_views.index, name='index'),

    # Категории
    path('category/<int:category_id>/', product_views.category_detail, name='category_detail'),

    # Товары
    path('product/<int:product_id>/', product_views.product_detail, name='product_detail'),
    path('product/<int:product_id>/add/', product_views.add_to_cart, name='add_to_cart'),

    # Авторизация
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    # Личный кабинет
    path('profile/', backend_views.profile, name='profile'),
    path('cart/', backend_views.cart_view, name='cart'),

    path('cart/remove/<int:item_id>/', backend_views.remove_from_cart, name='remove_from_cart'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
