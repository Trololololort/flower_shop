from django.core.validators import RegexValidator

cyrillic_validator = RegexValidator(
    regex=r'^[А-Яа-яЁё\- ]+$',
    message="Допустимы кириллица, пробел и тире.",
    code="invalid_registration",
)

latin_space_hyphen = RegexValidator(
    regex=r'^[A-Za-z0-9-]*$',
    message="Допустимы латиница, цифры и тире.",
    code="invalid_registration",
)

gte_6 = RegexValidator(
    regex=r'^(.{6})(.*)$',
    message="Не менее 6 символов.",
    code="invalid_registration",
)