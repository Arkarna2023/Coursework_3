from utils import load_operations, choose_operations, sort_operations
from datetime import datetime

path2operations = "operations.json"
all_operations = load_operations(path2operations)
executed_operations = choose_operations(all_operations)

for operation in sort_operations(executed_operations):
    operation_date = datetime.strptime(operation.get('date'), "%Y-%m-%dT%H:%M:%S.%f")
    print(operation_date.strftime("%d.%m.%Y"), operation.get('description'))

    if operation.get('from') is not None:
        operation_from = operation.get('from').split()
        if len(operation_from) == 3:
            account_number_from = operation_from[2]
            account_type_from = operation_from[0] + ' ' + operation_from[1]
        elif len(operation_from) == 2:
            account_number_from = operation_from[1]
            account_type_from = operation_from[0]
        account_number_from = (account_number_from[:4] + ' ' + account_number_from[5:7] + 2 * '*' + ' ' + 4 * '*' + ' '
+ account_number_from[-4:])
        print(account_type_from, account_number_from)

    if operation.get('to') is not None:
        operation_to = operation.get('to').split()
        if len(operation_to) == 3:
            account_number_to = operation_to[2]
            account_type_to = operation_to[0] + ' ' + operation_to[1]
        elif len(operation_to) == 2:
            account_number_to = operation_to[1]
            account_type_to = operation_to[0]
        account_number_to = (2*'*' + account_number_to[-4:])
        print(account_type_to, account_number_to)

    operation_amount = operation.get('operationAmount')
    operation_currency = operation_amount.get('currency')
    print(operation_amount.get('amount'), operation_currency.get('name'))
    print()
