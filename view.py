def input_number(title, min, max):
    number = input(title)
    if not number.isdigit():
        print('Вы ввели не цифру! Ведите номер требуемого действия!') 
        return None

    number = int(number)
    if min <= number <= max:
        return number


def menu_select(title, menu):
    while True:
        print(title)
        for index, item in enumerate(menu):
            print(f"{index + 1}: {item['title']}")
        
        index = input_number('Выберите пункт меню: ', 1, len(menu))
        if index:
            return menu[index - 1]
            