from django.urls import path
from shop import views
urlpatterns = [
    # path("products", views.ProductView.as_view(), name="products"),
    path("product-list", views.ProductListView.as_view(), name="product-list"),
    path("product-detail", views.ProductDetailsView.as_view(), name="product-detail"),
    path("product-cart", views.CartView.as_view(), name="product-cart"),
    path("product-checkout", views.CheckoutView.as_view(), name="product-checkout"),
    path('', views.shop, name="products"),
    path('<int:product_id>', views.product, name="product"),
    path('add_product/<int:product_id>', views.add_product, name="add_product"),
    # path('remove_product/<int:product_id>',
    #      views.remove_product, name="remove_product"),
    path('cart', views.cart, name="cart")
]
