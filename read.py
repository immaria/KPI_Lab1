import json



def info(library):  # Функція виводу вмісту бібліотеки: усіх книг та їх властивостей
    for book in library:  # Перебіг по книгам у бібліотеці
        get_info(book)  # Вивід інформації про книгу


def get_info(book):  # Функція отримання інформації про книгу
    for key, value in book.items():  # Перебіг по книгам у бібліотеці
        print(key, ' ', value)  # Виведення властивостей книги та їх значень
    print('\n')  # Розмежувач


def search(library):
    print("Уведіть назву книги, яку хочете знайти: ")
    name = input()
    for book in library:
        if book.get('Назва') == name:
            print('Книга є в бібліотеці')
            return
    print('Книги не знайдено.')


