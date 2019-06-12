import json


def save(library):  # Функція збереження вмісту бібліотеки у файл
    print("Уведіть назву файлу, у який хочете зберегти бібліотеку: ")
    file = open(input(), mode='w',  encoding='utf8')  # Файл призначений для зберігання
    json.dump(library, file, indent = 4 , sort_keys = True,
                      separators=(',', ': '), ensure_ascii = False)  # Передача вмісту масиву бібліотеки у файл призначення
    file.close()  # Закриття файлу



def add(library):  # Функція додавання книги у бібліотеку
    print('Уведіть назву')
    name = input()
    print('Уведіть ім\'я автора')
    author= input()
    print('Уведіть рік видання')
    year = int(input())
    print('Уведіть жанр')
    genre = input()
    book = {'Порядковий номер': len(library) + 1,
            'Назва': name,
            'Автор': author,
            'Рік видання': year,
            'Жанр': genre
            }
    library.append(book)  # Додавання до масиву бібліотеки книги


def remove(library):  # Функція видалення книги з бібліотеки
    print("Уведіть назву книги, яку хочете видалити: ")
    name = input()  # Ім'я книги для видалення
    for book in library:  # Пошук книги у бібліотеці
        if book.get('Назва') == name:  # Перевірка імені
            next = book.get('Порядковий номер')  # Визначення позиції книги для зменшення початкогвого номера на одиницю
            while next < len(library):  # Зсув позицій
                library[next].update({'Порядковий номер': library[next].get('Порядковий номер') - 1})
                next += 1
            library.remove(book)  # Видалення книги

