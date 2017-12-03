from django.shortcuts import render
from .models import Item
# Create your views here.
from django.http import HttpResponse, JsonResponse


def index(request):
    items = Item.objects.filter()
    return render(request, 'pizzashop/index.html', locals())


def item(request, item_id):
    item = Item.objects.get(id=item_id)
    session_key = request.session.session_key
    if not session_key:
        request.session.cicle_key()

    return render(request, 'pizzashop/item.html', locals())


def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    print(request.POST)

    return JsonResponse(return_dict)
