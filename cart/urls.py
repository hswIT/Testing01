from django.urls import path
from shop import views
from . import views

urlpatterns = [
    # path('remove_product/<int:product_id>',views.remove_product, name="remove_product"),
    path('', views.cart, name="carts"),
    path('empty_cart', views.empty_cart, name="empty_cart"),
    path('remove_product/<str:item_id>',
         views.remove_product, name="remove_product"),
    path('increase/<str:item_id>',
         views.increase, name="increase"),
    path('decrease/<str:item_id>',
         views.decrease, name="decrease"),
    path('back_to_cart', views.cart, name="back_to_cart"),
]
