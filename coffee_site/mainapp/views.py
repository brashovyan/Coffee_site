from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
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


def aja(request):
    fullName = request.GET.get('fullName')
    content = request.GET.get('content')
    total = request.GET.get('total')
    if(fullName != None and content != None and total != None):
        print(fullName)
        print(content)
        print(total)
        loh = "ты лох!"
        Order.objects.create(name=fullName, content=content, cost=total)
        data = {
            "loh": loh,
            # Data that you want to send to javascript function
        }
        return JsonResponse(data)
    else:
        return HttpResponseRedirect("/")




