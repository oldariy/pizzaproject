from .models import BasketItem


def getting_basket_info(request):
    session_key = request.session.session_key
    if not session_key:
        # workaround for newer Django versions
        request.session["session_key"] = 123
        # re-apply value
        request.session.cycle_key()

    items_in_basket = BasketItem.objects.filter(session_key=session_key, is_active=True, order__isnull=True)
    items_total_count = items_in_basket.count()

    return locals()
