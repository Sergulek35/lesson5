import platform
import os
from my_functions import menu, file_search, examination_folder, examination_files
from game import victory
from magazine import shop

while True:
    menu()

    menu_item = input('Выберите пункт меню: ')

    if menu_item == '1':
        user_input = input('Введите название папки: ')
        if not os.path.exists(user_input):
            os.mkdir(user_input)
            print(f'создана папка - {user_input}')
        else:
            print('Не удалось создать, такое имя уже есть!')

    elif menu_item == '2':
        examination_folder('удалить папку')

    elif menu_item == '3':
        examination_files('удалить файл')

    elif menu_item == '4':
        examination_folder('копировать папку')

    elif menu_item == '5':
        examination_files('копировать файл')

    elif menu_item == '6':
        print(os.listdir(os.getcwd()))

    elif menu_item == '7':
        file_search('папки')

    elif menu_item == '8':
        file_search('файлы')

    elif menu_item == '9':
        print(platform.platform())

    elif menu_item == '10':
        print('Программист')
    elif menu_item == '11':
        victory()

    elif menu_item == '12':
        shop()

    elif menu_item == '13':
        break

    else:
        print('Не правельный ввод!')
