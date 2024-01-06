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


def get_status_code(login):
    """
    Для организации проверки пароля без перезагрузки страницы.
    В зависимости от того, занят ли логин,
    отправить 204 или 409.
    """
    status_code = 204

    occupied_login = CustomUser.objects.filter(username=login).first()

    if occupied_login:
        status_code = 409

    return status_code