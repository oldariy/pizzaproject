from django.shortcuts import render, redirect
from pizzashop.forms import CheckoutContactForm
from .models import *
from django.http import JsonResponse


def index(request):
    items = Item.objects.filter()
    session_key = request.session.session_key
    # if not session_key:
    #     request.session['session_key'] = 123
    #     request.session.cycle_key()

    return render(request, 'pizzashop/index.html', locals())


def item(request, item_id):
    item = Item.objects.get(id=item_id)
    session_key = request.session.session_key
    if not session_key:
        request.session['session_key'] = 123
        request.session.cycle_key()

    return render(request, 'pizzashop/item.html', locals())


def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    print(request.POST)

    data = request.POST
    item_id = data.get('itemId')
    count = data.get('count')
    is_delete = data.get("is_delete")

    if is_delete == 'true':
        BasketItem.objects.filter(id=item_id).update(is_active=False)
    else:
        new_item, created = BasketItem.objects.get_or_create(session_key=session_key, item_id=item_id, is_active=True,
                                                             defaults={"count": count})

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


def checkout(request):
    session_key = request.session.session_key
    items_in_basket = BasketItem.objects.filter(session_key=session_key, is_active=True, order__isnull=True)
    form = CheckoutContactForm(request.POST or None)

    if request.POST:
        print(request.POST)
        if form.is_valid():
            print('yes, valid!')
            data = request.POST
            name = data.get('name')
            email = data.get('email')
            address = data.get('address')
            phone = data.get('phone')
            user, create = Customer.objects.get_or_create(first_name=name, phone=phone, email=email, address=address,
                                                          defaults={'first_name': name})

            order = Order.objects.create(customer=user, status='CR')

            for name, value in data.items():
                if name.startswith("item_in_basket_"):
                    item_in_basket_id = name.split("item_in_basket_")[1]
                    item_in_basket = BasketItem.objects.get(id=item_in_basket_id)
                    print(type(value))

                    item_in_basket.count = value
                    item_in_basket.order = order
                    item_in_basket.save(force_update=True)

                    OrderItem.objects.create(item=item_in_basket.item, count=item_in_basket.count,
                                             price_per_item=item_in_basket.price_per_item,
                                             total_price=item_in_basket.total_price,
                                             order=order)

            items_in_basket = BasketItem.objects.filter(session_key=session_key).delete()
            return redirect('/thanks/')

        else:
            print('NO, NOT VALID!')
    return render(request, 'pizzashop/checkout.html', locals())


def thanks(request):
    session_key = request.session.session_key
    return render(request, 'pizzashop/thanks.html', locals())