from django.shortcuts import render
from .models import Item
# Create your views here.
from django.http import HttpResponse


def index(request):
    items = Item.objects.filter()
    return render(request, 'pizzashop/index.html', locals())
