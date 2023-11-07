import json
import os

def load_operations(path):
    """
    загружает список операций для чтения
    :param path:
    :return:
    """
    with open(path, "r", encoding="utf-8") as file:
        all_operations = json.load(file)
        return all_operations

def choose_operations(all_operations):
    """
    выбирает операции (EXECUTED)
    :return:
    """
    executed_operations = []
    for operation in all_operations:
        if operation.get('state') == 'EXECUTED':
            executed_operations.append(operation)
    return executed_operations








