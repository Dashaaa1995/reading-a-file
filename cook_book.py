from pprint import pprint


# Задача №1
def create_cook_book(file_name):
    cook_book = {}

    try:
        # читаем файл. разбиваем на строки. записываем строки в список lst для более удобной работы
        with open(file_name, encoding='utf-8') as f:
            list = [line.strip() for line in f]

        # тут долго ломал голову как лучше начать и взять название блюда... ничего лучше в голову не пришло...
        for i, c in enumerate(list):
            if c.isdigit():
                # если элемент == цифра ==> берем название блюда из предшествующего элемента
                cook_book[list[i-1]] = []

                # собираем ингридиенты в срезе с индекса после кол-ва ингр-ов до : индекс + кол-во ингр-ов + 1
                for slice in list[i+1:i+int(c)+1]:
                    ingredient_name = slice.split('|')[0]
                    quantity = int(slice.split('|')[1])
                    measure = slice.split('|')[2]

                    cook_book[list[i-1]].append({'ingredient_name':ingredient_name,
                                                'quantity':quantity,
                                                'measure':measure})
        return cook_book

    except FileNotFoundError:
        return(f'Файл: {file_name} не найден.')
    except Exception as error:
        return f'Ошибка - {error}'


# Задача №2
# в качестве второго аргумента решил передавать результат работы функции
def shop_list_by_dishes(dishes, cooking_book, person_count):
    dict = {}

    for key in cooking_book.keys ():
        for dish in dishes:
            if key == dish:
                for dictionary in cooking_book[key]:
                    # пробежимся по ключам словаря
                    ing_name = dictionary['ingredient_name']

                    try:
                        dict[ing_name]['quantity'] += (dictionary['quantity'] * person_count)
                    except:
                        dict[ing_name] = {'measure': dictionary['measure'],
                                              'quantity': dictionary['quantity'] * person_count}

    return dict


#####################################
# ВЫВОД
# Задача №1
print('Задача №1:\n')
pprint(create_cook_book('recipes.txt'))
print('\n' * 3)


# Задача №2
print('Задача №2:\n')
pprint(shop_list_by_dishes(['Омлет', 'Запеченный картофель'], create_cook_book('recipes.txt'), 2))

