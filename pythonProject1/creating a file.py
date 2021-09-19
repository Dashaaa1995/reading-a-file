import os

def select_files():
    """Отбирает нужные файлы с директории"""
    selection_list = []
    directory_files = os.listdir()
    for file in directory_files:
        if file == '1.txt' or file == '2.txt' or file == '3.txt':
            selection_list.append(file)
    return selection_list


def sorting_files(selection_list):
    """ Сортирует файлы по количеству строк"""
    total_dict = {}
    for file in selection_list:
        with open(file, encoding='utf-8') as f:
            a = f.readlines()
            total_dict[file] = len(a)
    sorted_size = sorted(total_dict.items(), key=lambda item: item[1])
    return sorted_size


def merger(sorted_size):
    """Извлекает данные из файлов и объединяет их в списке"""
    dict_new = []
    for i in sorted_size:
        file = i[0]
        with open(file, encoding='utf-8') as f:
            a = f.read()
            dict_new.append(a)
    return dict_new


def writing_to_file(dict_l):
    """Создает файл и записывает в него данные"""
    my_file = open('n_fail.txt', 'w', encoding='utf-8')
    my_file.close()
    for i in dict_l:
        with open('n_fail.txt', 'a') as document:
            document.write(i)


selection_list = select_files()
sorted_size = sorting_files(selection_list)
dict_l = merger(sorted_size)
writing_to_file(dict_l)