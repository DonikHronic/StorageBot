def convert_text(inner_text: str):
    """
    Транслитерирует текст из русских символов в текст из английских символов
    :param inner_text: str
    :return: transliterated_text
    """

    lower_case_letters = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "е": "e",
        "ё": "e",
        "ж": "zh",
        "з": "z",
        "и": "i",
        "й": "y",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "h",
        "ц": "ts",
        "ч": "ch",
        "ш": "sh",
        "щ": "sch",
        "ъ": "",
        "ы": "y",
        "ь": "",
        "э": "e",
        "ю": "yu",
        "я": "ya",
        " ": "_",
    }

    transliterated_text = ""
    for index, char in enumerate(str(inner_text).lower()):
        if char in lower_case_letters:
            transliterated_text += lower_case_letters[char]
        else:
            transliterated_text += char

    return transliterated_text


def image_path(instance, filename):
    return f"products/{convert_text(instance.name)}/{filename}"
