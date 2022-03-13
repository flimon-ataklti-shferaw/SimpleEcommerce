from django.shortcuts import render

from .models import Cart


def cart_view(request):
    #del request.session['cart_id']
    cart_id = request.session.get("cart_id", None)
    if cart_id is None:
        cart_obj = Cart.objects.create()
        request.session['cart_id'] = cart_obj.id
        print('cart created')
    else:
        print('cart exist')
        cart_obj = Cart.objects.get(id=cart_id)
    return render(request, "carts/cart.html", {})
