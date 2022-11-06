
import db


def input(titles):
    result = []
    for title in titles:
        result.append(input(f'{title}: '))
    return result


def view_student():
    print('Контакты учеников')
    data = db.read('student_base.csv')
    # ['ID', 'Фамилия', 'Имя', 'Отчество', 'Класс']
    print(data)


def view_teacher():
    print('Контакты учителей')
    data = db.read('teacher_base.csv')
    # ['ID', 'Фамилия', 'Имя', 'Отчество', 'Предмет']
    print(data)

def add_student():
    print('Добавляем контакт ученика. Введите:')
    student = input([
        'Фамилию',
        'Имя',
        'Отчество',
        'Класс'
    ])
    student_id = db.append('student_base.csv', student)
    print(f'Ученик успешно добавлен с id: {student_id}')


def add_teacher():
    print('Добавляем контакт учителя. Введите:')
    teacher = input([
        'Фамилию',
        'Имя',
        'Отчество',
        'Предмет',
    ])
    teacher_id = db.write('teacher_base.csv', teacher)
    print(f'Учитель успешно добавлен с id: {teacher_id}')

# Для того чтобы узнать необходимый id для действий можно воспользоваться просмотром списка

def see_mark():
    student = input('Для просмотра оценок введите id:') 
    marks = db.read('mark_base.csv')
    search = False
    for data in marks:
        if student in data:
            print('Ваши оценки: ', data)
            search = True
    if not search:
        print('Фамилия в базе отсутствует!')


def mark():
    print('Выставляем оценку:')
    # mark = 
    mark = db.write('mark_base.csv', mark)
    print('Оценка успешно добавлена')
    

def delete_teacher(): 
    print('Удаляем контакт учителя!')
    delete = input('id учителя: ')
    delete = db.remove('teacher_base.csv', delete)
    print(f'Успешно удален контакт учителя с {delete}')


def delete_student(): 
    print('Удаляем контакт ученика!')
    delete = input('id student: ')
    delete = db.remove('student_base.csv', delete)
    print(f'Успешно удален контакт ученика с id: {delete}')

