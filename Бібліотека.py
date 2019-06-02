import write
import read
import json


def load():
    global library  # Функція завантаження бібліотеки з файлу
    print("Уведіть назву файлу, з якого хочете завантажити бібліотеку: ")
    file = open(input(), mode='r')  # файл завантаження
    library = json.load(file)  # Передача вмісту файлу у масив бібліотеки
    file.close()  # Закриття файлу


library = []
while True:
    try:

        print('Зробіть вибір:\n 1 - для завантаження бібліотеки з файлу,\n 2 - для збереження бібліотеки,'
              '\n 3 - для додавання книги до бібліоеки,\n 4 - для видалення книги з бібліотеки,'
              '\n 5 - для отримання інформації про вміст бібліотеки,'
              '\n 6 - для пошуку книги за іменем,\n 7 - для виходу')
        choice = int(input())
        if choice == 1:
            load()
        elif choice == 2:
            write.save(library)
        elif choice == 3:
            write.add(library)
        elif choice == 4:
            write.remove(library)
        elif choice == 5:
            read.info(library)
        elif choice == 6:
            read.search(library)
        elif choice == 7:
            break
        else:
            print('Некоректний вибір')
    except ValueError:
        print('Дані введені неправильно')
    except Exception as e:
        print(e)




