import phonebook
import view



def start():
    ph_b = phonebook.Phonebook('text_book.txt')
    while True:
        print(view.main_menu())
        command = int(input('Выберите пункт меню: '))
        match command:
            case 1:
                view.print_contact_list(ph_b)
            case 2:
                contact = view.input_contact()
                ph_b.new_contact(contact)
            case 3:
                request = input('Введите поисковый запрос: ')
                result = ph_b.search(request)
                view.print_contact_list(result)
            case 4:
                view.print_contact_list(ph_b)
                index = view.get_integer('Введите номер контакта, который будете изменять: ')
                contact_details = view.input_contact('(или нажмите Enter, чтобы оставить без изменений)')
                ph_b.edit_contact(index-1, contact_details['name'], contact_details['number'], contact_details['comment'])
            case 5:
                view.print_contact_list(ph_b)
                index = view.get_integer('Введите номер контакта, который надо удалить: ')
                ph_b.delete(index-1)
            case 6:
                ph_b.save()
            case 7:
                break


