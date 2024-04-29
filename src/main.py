import json

def load_operations():
    """вытаскиваем из json"""
    with open('operations.json', ) as f:
        return json.load(f)

list_operation = []
list_operation_exe = []

def executed_operations():
    """выбираем только "EXECUTED" и складывем в отдельный список"""
    for operation in load_operations():
        if operation.get("state") == "EXECUTED":
            list_operation_exe.append(operation)

    return list_operation_exe

def sort_date():
    """сортируем по дате и выводим последние 5 операций"""
    sorted_data = sorted(executed_operations(), key=lambda x: x['date'], reverse=True)

    return sorted_data

s = sort_date()
def main():
    if get_from_(i) != None:
        print(f"{get_date(i)} {get_description(i)} \{get_from_(i)} -> {get_to(i)} \{get_amount(i)} {get_currency(i)}")
    else:
        print(f"{get_date(i)} {get_description(i)} \-> {get_to(i)} \{get_amount(i)} {get_currency(i)}")