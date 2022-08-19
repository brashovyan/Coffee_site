from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Order, Product


def index(request):
    if request.method == "POST":
        email = request.POST.get('email')
        print(email)
        return render(request, 'mainapp/index.html')
    else:
        return render(request, 'mainapp/index.html')


def order(request):
    products = Product.objects.all()
    return render(request, 'mainapp/order.html', {"products": products})


def success(request, fullName, content, total):
    print(fullName)
    print(content)
    print(total)
    Order.objects.create(name=fullName, content=content, cost=total)

    return HttpResponseRedirect("/")

