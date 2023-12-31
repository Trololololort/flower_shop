from carts.service import get_cart_contents
from goods.models import Goods


def are_there_enough_goods(user, goods_id):
    """
    Нельзя добавить в корзину товаров больше, чем есть в наличии.
    Пользователь добавляет товар в корзину по одной штуке.

    Проверить, хватает ли товара, если сложить то, что есть в корзине,
    и 1 шт.
    """
    goods = Goods.objects.filter(pk=goods_id).first()
    all_goods_in_cart = get_cart_contents(user)
    goods_in_cart = all_goods_in_cart.filter(goods=goods_id).values_list("quantity", flat=True)

    TO_BE_ORDERED = 1

    result = goods.stock - TO_BE_ORDERED

    if goods_in_cart:
        goods_in_cart = goods_in_cart[0]
        result -= goods_in_cart

    return result >= 0
