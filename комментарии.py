# Однострочный.
# Все комментарии с заглавной буквы, не больше 72 знаков.

# Не злоупотреблять комментариями

"""Doc string"""


def doc_string():
    """
    Многострочный комментарий для документации.
    Описание пакета или модуля, обычно пишут в __init__.py файле пакета,
    но не только. Также используется для описания функций и классов.
    """


print(doc_string.__doc__)
print(__doc__)
