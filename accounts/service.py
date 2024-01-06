from accounts.models import CustomUser


def create_user(surname,
                name,
                partonymic,
                login,
                email,
                rules,
                password):

    user = CustomUser.objects.create(last_name=surname,
                                     first_name=name,
                                     partonymic=partonymic,
                                     username=login,
                                     password=password,
                                     email=email,
                                     rules=rules)
    user.set_password(user.password)  # Сохранить хэшированный пароль.
    user.save()


def is_login_occupied(login):
    """
    Для организации проверки пароля без перезагрузки страницы.
    В зависимости от того, занят ли логин,
    отправить 204 или 409.
    """
    status = {"status": 204, "message": "Login is free"}

    occupied_login = CustomUser.objects.filter(username=login).first()

    if occupied_login:
        status = {"status": 409, "message": "Login is occupied"}

    return status