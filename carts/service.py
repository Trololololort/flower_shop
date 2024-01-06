from carts.models import Cart
from goods.models import Goods


def get_cart_contents(user):
    """
    В корзине лежат товары пользователя,
    которым еще не создан заказ.
    """
    object_list = Cart.objects.filter(user=user).filter(order=None)

    return object_list


def add_goods_to_cart(goods_id, user, addend):
    goods = Goods.objects.filter(pk=goods_id).first()

    if goods:

        the_goods_already_in_cart = Cart.objects.filter(user=user, goods=goods, order=None).first()

        if the_goods_already_in_cart:
            the_goods_already_in_cart.quantity = (the_goods_already_in_cart.quantity + addend)

            if the_goods_already_in_cart.quantity == 0:
                the_goods_already_in_cart.delete()
            else:
                the_goods_already_in_cart.save()

        else:
            Cart.objects.create(user=user, goods=goods, quantity=1)
        status = 200
        act = "добавлен в корзину" if addend > 0 else "убран из корзины"
        message = 'Товар "{}" {}.'.format(goods.name, act)
    else:
        status = 400
        message = "Wrong goods id"

    return {"status": status, "message": message}



