from django.shortcuts import render
from .models import Item, BasketItem
# Create your views here.
from django.http import HttpResponse, JsonResponse


def index(request):
    items = Item.objects.filter()
    return render(request, 'pizzashop/index.html', locals())


def item(request, item_id):
    item = Item.objects.get(id=item_id)
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    return render(request, 'pizzashop/item.html', locals())


def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    print(request.POST)

    data = request.POST
    item_id = data.get('itemId')
    count = data.get('count')
    new_item = BasketItem.objects.create(session_key=session_key, item_id=item_id, count=count)
    items_total_count = BasketItem.objects.filter(session_key=session_key, is_active=True).count()
    return_dict["items_total_count"] = items_total_count
    return JsonResponse(return_dict)
