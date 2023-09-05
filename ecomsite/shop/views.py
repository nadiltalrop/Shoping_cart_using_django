from django.shortcuts import render
from django.core.paginator import Paginator

from .models import *


def index(request):
    instances = Product.objects.filter(is_deleted=False)

    # search
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        instances = instances.filter(title__icontains=item_name)

    # paginator
    paginator = Paginator(instances,8)
    page = request.GET.get('page')
    instances = paginator.get_page(page)   

    return render(request, 'shop/index.html', {'instances': instances})


def detail(request, id):
    instance = Product.objects.get(id=id)

    return render(request, 'shop/detail.html', {'instance': instance})


def checkout(request):
    if request.method == 'POST':
        items = request.POST.getlist('items',"")
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        address = request.POST.get('address',"")
        city = request.POST.get('city',"")
        state = request.POST.get('state',"")
        zipcode = request.POST.get('zipcode',"")
        total = request.POST.get('total',"")

        order = Order(items=items,name=name, email=email, address=address, city=city, state=state, zipcode=zipcode,total=total)
        order.save()


    return render(request, 'shop/checkout.html')