from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in the shopping cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51H94UcI7bZXactEOXOqQyUEJhrMZHT1K8QCSKJ8cO3Hn7CIb6V1PM0x0CwR8GPexF5G72CDli2gWBpYmFsqdChuA000ql874JU',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)