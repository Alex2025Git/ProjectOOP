import json

from src.models import Category


def reading_json(path):
    """Функция для получения данных по категориями и товарам из файла JSON
    принимает в качестве аргумента путь к файлу в формате JSON"""

    with open(path, encoding="UTF8") as file:
        data_file = json.load(file)
    list_object = []
    for srt_json in data_file:
        get_object = Category(
            srt_json.get("name"), srt_json.get("description"), srt_json.get("products")
        )
        list_object.append(get_object)

    return list_object
