class Contact:
    def __init__(self, name: str, phone: str, comment: str):
        self.name = name
        self.phone = phone
        self.comment = comment

    def to_txt_storage(self):
        return f'{self.name}|{self.phone}|{self.comment}'

    def __str__(self):
        return f'{self.name:<20} - {self.phone:<20} - {self.comment:<20}'


class Phonebook:
    def __init__(self, path: str):
        self.path = path
        self.contact_list = []
        self.open()

    def open(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            text = file.readlines()
        for person in text:
            new_contact = person.strip().split('|')
            self.contact_list.append(Contact(*new_contact))# (Contact(new_contact[0], new_contact[1], new_contact[2]))
            # - звёздочка показывает, что в качестве аргументов идут элементы итерируемого объекта new_contact

    def save(self):
        text = '\n'.join([person.to_txt_storage() for person in self.contact_list])
        with open(self.path, 'w', encoding='UTF-8') as file:
            file.write(text)

    def new_contact(self, contact_info: dict):
        self.contact_list.append(Contact(contact_info['name'], contact_info['number'], contact_info['comment']))

    def search(self, request: str):
        result = []
        is_found = False
        for person in self.contact_list:
            if request.lower() in person.to_txt_storage().lower():
                result.append(f'{person}')
                is_found = True
        if is_found:
            return '\n'.join(result)
        else:
            return 'Контакт не найден'

    def edit_contact(self, index: int, name: str, number: str, comment: str):
        name = name if name != '' else self.contact_list[index].name
        number = number if number != '' else self.contact_list[index].phone
        comment = comment if comment != '' else self.contact_list[index].comment
        self.contact_list[index] = Contact(name, number, comment)

    def delete(self, index: int):
        self.contact_list.pop(index)

    def __str__(self):
        result = ''
        i = 0
        for person in self.contact_list:
            i += 1
            result += f'{i}. {person}\n'
        return result[:-2]
