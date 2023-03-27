def print_contact_list(contact_list):
    print(contact_list)


def main_menu():
    return '''Выберите пункт меню:
    1. Отобразить все контакты
    2. Добавить новый контакт
    3. Найти контакт
    4. Изменить контакт
    5. Удалить контакт
    6. Сохранить изменения
    7. Выход'''


def get_integer(message: str):
    while True:
        result = input(message)
        if result.isdigit():
            return int(result)
        else:
            print("Нужно ввести число")


def get_menu_command():
    print(main_menu())
    menu_len = len(main_menu().split('\n')) - 1
    while True:
        result = get_integer("Введите номер пункта меню: ")
        if result <= menu_len:
            return result
        else:
            print(f'Введённое число должно быть не меньше 1 и не больше {menu_len}')

def input_contact(additional = ''):
    contact = {}
    contact['name'] = input(f'Введите имя контакта {additional} ')
    contact['number'] = input(f'Введите номер телефона {additional} ')
    contact['comment'] = input(f'Введите комментарий {additional} ')
    return(contact)