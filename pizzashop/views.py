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
    # new_item = BasketItem.objects.create(session_key=session_key, item_id=item_id, count=count)
    new_item, created = BasketItem.objects.get_or_create(session_key=session_key, item_id=item_id, is_active=True, defaults={"count": count})
    if not created:
        print("not created")
        new_item.count += int(count)
        new_item.save(force_update=True)

    items_in_basket = BasketItem.objects.filter(session_key=session_key, is_active=True, order__isnull=True)
    items_total_count = items_in_basket.count()
    return_dict["items_total_count"] = items_total_count
    return_dict["items"] = list()

    for product in items_in_basket:
        product_dict = dict()
        product_dict["id"] = product.id
        product_dict["name"] = product.item.title
        product_dict["price_per_item"] = product.price_per_item
        product_dict["count"] = product.count
        return_dict["items"].append(product_dict)

    return JsonResponse(return_dict)
