from django.shortcuts import render
from .models import Item
# Create your views here.
from django.http import HttpResponse


def index(request):
    items = Item.objects.filter()
    return render(request, 'pizzashop/index.html', locals())


def item(request, item_id):
    item = Item.objects.get(id=item_id)
    return render(request, 'pizzashop/item.html', locals())
