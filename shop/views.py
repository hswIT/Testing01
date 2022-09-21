# from itertools import product
import logging
from .models import Product
from django.views import View
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from dj_shop_cart.cart import get_cart_class
from django.http import HttpRequest


def shop(request):
    products = Product.objects.order_by('-list_date')
    paginator = Paginator(products, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'products': paged_listings
    }

    return render(request, 'shop/products.html', context)

# add product(request, product_id) by Matt


def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product
    }
    return render(request, 'shop/product-detail.html', context)


################# NEW ADDING ###################################
Cart = get_cart_class()


def view(request: HttpRequest):
    cart = Cart.new(request)


@require_POST
def add_product(request: HttpRequest, product_id):
    cart = Cart.new(request)
    product = get_object_or_404(
        Product.objects.all(), id=request.POST["product"])
    #variant = get_variant(request)
    quantity = int(request.POST.get("quantity", 0))
    cart.add(product, quantity=quantity)  # variant=variant,
    # a Cartitem with specific product would be stored in cart
    return redirect("cart")


@require_POST
def decrement_product(request):
    cart = Cart.new(request)
    product = get_object_or_404(
        Product.objects.all(), id=request.POST["product"])
    quantity = int(request.POST.get("quantity", 0))
    cart.add(product, quantity=quantity)  # variant=get_variant(request)
    return redirect('shop/products.html')


# @require_POST
# def remove_product(request: HttpRequest, product_id):
#     cart = Cart.new(request)
#     product = get_object_or_404(
#         Product.objects.all(), id=request.POST["product"])
#     cart.remove(product)  # variant=get_variant(request)
#     return redirect('carts')


# @require_POST
# def empty_cart(request):
#     cart = Cart.new(request)
#     cart.empty()
#     return redirect('shop/products.html')


def cart(request):
    return render(request, 'shop/cart.html')


##################################################################

class ProductView(View):
    def get(self, request):
        gretting = {"title": "Product"}
        return render(request, 'shop/products.html', gretting)


class ProductListView(View):
    def get(self, request):
        gretting = {"title": "Product List"}
        return render(request, 'shop/product-list.html', gretting)


class ProductDetailsView(View):
    def get(self, request):
        gretting = {"title": "Product Details"}
        return render(request, 'shop/product-detail.html', gretting)


class CartView(View):
    def get(self, request):
        gretting = {"title": "Cart "}
        return render(request, 'shop/cart.html', gretting)


class CheckoutView(View):
    def get(self, request):
        gretting = {"title": "Checkout"}
        return render(request, 'shop/checkout.html', gretting)
