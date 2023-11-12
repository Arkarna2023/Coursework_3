import json
from datetime import datetime

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

def sorted_by_date(op):
    return datetime.strptime(op['date'],  '%Y-%m-%dT%H:%M:%S.%f')

def sort_operations(executed_operations):
    """
    сортирует операции по дате и выбирает 5 последних
    :return:
    """
    sorted_operations = sorted(executed_operations, key=lambda op: sorted_by_date(op), reverse=True)
    return sorted_operations[:5]





