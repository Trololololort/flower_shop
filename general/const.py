from enum import Enum
from enum import auto


class RESULT(Enum):
    """
    Результат работы метода.
    """
    SUCCESS = auto()
    FAILURE = auto()
