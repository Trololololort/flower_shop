from enum import Enum

CHOICES_DICT = {
    "added": "Дата поступления в продажу",
    "origin": "Страна происхождения",
    "category": "Вид товара",
    "price": "Цена",
}


class STATUC_CODES(Enum):
    # Статусы ответов сервера:
    # достаточно ли товара для добавления
    # в корзину.

    ENOUGH = {"code": 204, "message": "Enough goods"},
    LACK = {"code": 409, "message": "Lack of goods"},
