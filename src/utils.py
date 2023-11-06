import json
import os

def load_operations(path):
    """
    загружает список операций для чтения
    :param path:
    :return:
    """
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)
