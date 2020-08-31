from django.shortcuts import render, redirect
from products.models import Product


def about(request):
    return render(request, 'about.html')
