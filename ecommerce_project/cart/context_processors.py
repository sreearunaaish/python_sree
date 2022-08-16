from .models import Cart,Cart_item
from . views import _cart_id

def counter(request):
    item_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart=Cart.objects.filter(cart_id=_cart_id(request))
            car_items=Cart_item.objects.all().filter(cart=cart[:1])
            for cartitem in car_items:
                item_count += cartitem.quantity
        except Cart.DoesNotExist:
            item_count=0
    return dict(item_count=item_count)

