

#Мой вариант
# def get_shop_list_by_dishes(dishes, person_count):
#     lc_dict2buy = {}
#     list_ing4dish = {}
#     loc_dict_cook_book = read_cook_book()
#     for dish in dishes:
#         if (dish == '' or dish == ' '):
#             continue
#         list_ing4dish = loc_dict_cook_book.get(str(dish))   #получен списко ингредиентов для блюда
#         #print (list_ing4dish)
#         for ing in list_ing4dish:
#             if ing['ingridient_name'] not in lc_dict2buy.keys():
#                 lc_dict2buy[ing['ingridient_name']] = {'measure': ing['measure'], 'quantity': 0}
#             lc_dict2buy[ing['ingridient_name']]['quantity'] = lc_dict2buy[ing['ingridient_name']]['quantity'] + ( int(ing['quantity'] )) * person_count
#     return lc_dict2buy

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingridient in cook_book[dish]:
                new_shop_list_item = dict(ingridient)
                #print(new_shop_list_item)
                new_shop_list_item['quantity'] *= person_count
                if new_shop_list_item['ingridient_name'] not in shop_list:
                    shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
                else:
                    shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list



def get_dishes():
    loc_list = []
    loc_list.append('Запеченный картофель')
    loc_list.append('Омлет')
    return loc_list


def get_persons_num():
    return 2


def read_cook_book():
    loc_dict = {}
    lv_dish_name = ''
    lv_ing_num = 0
    lv_ing_proc = 0
    lv_ingredient_line = ''

    with open('book.txt', 'rt', encoding='utf-8') as cook_book_file:
        for line in cook_book_file:
            lv_dish_name = line.strip() #название
            #print (lv_dish_name)
            list_ing4dish = []
            lv_ing_num = cook_book_file.readline().strip()  # номер
            #print(lv_ing_num)
            lv_ing_proc = 0
            while (int(lv_ing_num) > lv_ing_proc):
                dict_ing_info = {}
                list_ing_info = []
                lv_ingredient_line = cook_book_file.readline().strip()  # строка ингеридентом
                #print(lv_ingredient_line)
                list_ing_info = lv_ingredient_line.split('|') # раздел строки по символу
                #print(list_ing_info)
                dict_ing_info['ingridient_name'] = list_ing_info[0]
                dict_ing_info['quantity'] = int(list_ing_info[1])
                dict_ing_info['measure'] = list_ing_info[2]
                list_ing4dish.append(dict_ing_info)
                lv_ing_proc += 1
            loc_dict[str(lv_dish_name)] = list_ing4dish
            cook_book_file.readline()
    return loc_dict

def read_cook_book_anc_calc_list():
    loc_dict_cook_book = read_cook_book()
    print(loc_dict_cook_book)

    print('Получаем количество блюд и персон')
    loc_list_dishes = get_dishes()
    loc_persons_num = get_persons_num()

    print('Формируем список ингридиентов')
    cook_book = read_cook_book()
    loc_list2buy = get_shop_list_by_dishes(loc_list_dishes, loc_persons_num, cook_book)
    #Мой вариант
    #loc_list2buy = get_shop_list_by_dishes(loc_list_dishes, loc_persons_num)

    print(loc_list2buy)

print('=====Начало работы программы=====')
read_cook_book_anc_calc_list()
print('=====Завершение работы программы=====')