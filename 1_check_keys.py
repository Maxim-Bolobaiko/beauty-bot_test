import re


def check_keys(text, list_keys):
    found_keys = re.findall(r"\{(\w+)\}", text)
    errors = []

    open_brackets = text.count("{")
    close_brackets = text.count("}")
    if open_brackets != close_brackets:
        errors.append(
            "Ошибка: проверьте открывающие и закрывающие фигурные скобки!"
        )

    invalid_keys = [key for key in found_keys if key not in list_keys]
    if invalid_keys:
        errors.append(
            "В следующих ключах, возможно, ошибка:\n" + "\n".join(invalid_keys)
        )

    if errors:
        return "\n".join(errors)

    return text


test_text = """{name}, ваша запись изменена:
⌚️ {day_month} в {start_time}
👩 {master}
Услуги:
{services}
управление записью {record_link}"""

list_keys = [
    "name",
    "day_month",
    "day_of_week",
    "start_time",
    "end_time",
    "master",
    "services",
]
