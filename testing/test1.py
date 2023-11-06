import doctest
from morse import LETTER_TO_MORSE


def encode(message: str) -> str:
    """
    Кодирует строку в соответствии с таблицей азбуки Морзе.

    >>> encode("SOS") # doctest: +NORMALIZE_WHITESPACE
    '... --- ...'
    >>> encode("SOS🐷") # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    KeyError
    """
    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]

    return ' '.join(encoded_signs)


if __name__ == "__main__":
    doctest.testmod()
