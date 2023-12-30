from carts.models import Cart


def get_cart_contents(user):
    # user : int | AbstractUser
    object_list = Cart.objects.filter(user=user).filter(order=None)

    return object_list
