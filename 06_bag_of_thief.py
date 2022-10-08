import sys

def print_help():
    print("""
Использование программы в командной строке:

[1]              [2]
06_bag_of_thief.py [filename]

[1] - вызов самой программы
[2] - аргумент программы - имя файла с входными данными [filename]

Пример вызова:
06_bag_of_thief.py things_params.csv

Формат [filename] соответствует стандартному csv-файлу.

В [filename] должны быть следующие данные:
Верхняя строка содержит названия столбцов, не значима для программы
Каждая последующая строка содержит данные о типе вещи на "складе"
Первый столбец содержит данные о массе вещи, целочисленный!
Второй столбец содержит данные о ценности вещи, целочисленный.

Разделитель данных - ; - точка с запятой

Запрос к пользователю о грузовместимости сумки грабителя

Вывод программы: набор вещей с максимальной суммарной ценностью
""")

def check_number_of_arguments():
    if 2 != len(sys.argv): return False
    
def check_and_prepare_data(data):
    # Convertation to numbers
    for i in range(1, len(data)):
        for j in range(len(data[i])):
            try:
                data[i][j] = int(data[i][j])
            except ValueError:
                print("""ОШИБКА!
        
В ячейке матрицы данные которые не получается конвертировать в число!\n\nИндексы:""", i, j, "\nДанные:", data[i][j], "\n")
                exit()

def load_data_from_file():
    data_file = open(sys.argv[1])
    data = [] 
    for i in data_file:
        data.append(i.strip().split(";"))
        
    data_file.close()
    check_and_prepare_data(data)
    return data

def output_data_to_stdout(data):
    for i in range(1, len(data)):
        print("No:", data[i][0], "\tWeight:", data[i][1], "\tCost:", data[i][2])

def ask_user_about_weight_to_go():
    print("Максимальная грузоподъёмность грюкзака:", end="")
    try:
        max_weight = int(input())
        return max_weight
    except:
        print("Введите число!")
        return None
        
def find_out_what_max_cost_can_be_snatched(data, max_weight):
    max_cost_by_weight = []
    max_cost_by_weight.append(0)
    
    for curr_weight in range(1, max_weight + 1):
        to_make_choise = []
        for item_number in range(1, len(data)):
            item_weight = data[item_number][1]
            item_cost   = data[item_number][2]
            
            positive_condition_to_use = curr_weight - item_weight
            if positive_condition_to_use >= 0:
                to_make_choise.append(item_cost + max_cost_by_weight[positive_condition_to_use])
            else: pass
        if len(to_make_choise) == 0:
            max_cost_by_weight.append(0)
            continue
        
        #print(curr_weight, to_make_choise, max(to_make_choise))
        max_cost_by_weight.append(max(to_make_choise))
    
    print("Стоимость похищенного:", max_cost_by_weight[-1])

        
if __name__ == "__main__":
    print("Bag of thief!")
    
    if(check_number_of_arguments() == False):
        print_help()
        exit()
    data = load_data_from_file()
    output_data_to_stdout(data)
    
    max_weight = None
    while True:
        max_weight = ask_user_about_weight_to_go()
        if max_weight == None: continue
        else: break
        
    find_out_what_max_cost_can_be_snatched(data, max_weight)