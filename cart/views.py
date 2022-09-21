from dj_shop_cart.cart import get_cart_class
from django.http import HttpRequest
from shop.models import Product
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.http import HttpRequest
import logging

Cart = get_cart_class()


def view(request: HttpRequest):
    cart = Cart.new(request)


@require_POST
def empty_cart(request):
    cart = Cart.new(request)
    cart.empty()
    return redirect('carts')


def cart(request):
    return render(request, 'shop/cart.html')


@require_POST
def remove_product(request, item_id):
    cart = Cart.new(request)
    # product = get_object_or_404(
    #     Product.objects.all(), id=request.POST["product"])
    cart.remove(item_id)  # variant=get_variant(request)
    return redirect('carts')


@require_POST
def increase(request, item_id):
    cart = Cart.new(request)
    product = get_object_or_404(
        Product.objects.all(), id=request.POST["aaaa"])
    # quantity = int(request.POST.get("quantity2"))
    quantity = 1
    cart.increase(item_id, quantity)
    return redirect("cart")


@require_POST
def decrease(request, item_id):
    cart = Cart.new(request)
    # product = get_object_or_404(
    #     Product.objects.all(), id=request.POST["bbbb"])
    # quantity = int(request.POST.get("quantity2"))
    cart.remove(item_id, quantity=1)
    return redirect("cart")
