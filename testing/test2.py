import pytest
from morse import MORSE_TO_LETTER


def decode(morse_message: str) -> str:
    """
    Декодирует строку из азбуки Морзе в английский
    """
    decoded_letters = [
        MORSE_TO_LETTER[letter] for letter in morse_message.split()
    ]

    return ''.join(decoded_letters)


@pytest.mark.parametrize("morse_message, expected", [
    ("-- . --- .--", "MEOW"),
    (".. .-.. --- ...- . .--. .. --. ...", "ILOVEPIGS")
    ])
def test_decode(morse_message, expected):
    assert decode(morse_message) == expected


@pytest.mark.parametrize(
    "morse_message", [
        "meow",
        ".........."
    ])
def test_decode_invalid_inputs(morse_message):
    with pytest.raises(KeyError):
        decode(morse_message)


if __name__ == "__main__":
    pytest.main()
