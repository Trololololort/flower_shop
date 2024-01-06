from carts.models import Cart


def get_cart_contents(user):
    """
    В корзине лежат товары пользователя,
    которым еще не создан заказ.
    """
    object_list = Cart.objects.filter(user=user).filter(order=None)

    return object_list


