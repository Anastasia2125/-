import random
from os import remove
from sys import builtin_module_names

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Редактировать данные по оценкам
        5. Удалить данные по оценкам
        6. Редактировать данные по предметам
        7. Удалить данные по предметам
        8. Редактировать данные по ученикам
        9. Удалить данные по ученикам
        10. Вывод информации по всем оценкам для ученика
        11. Вывод среднего балла по каждому предмету по определенному ученику
        12. Вывести средний балл по предмету
        13. Вывести рейтинг учеников 
        14.Выход из программы
        ''')
while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 4:
        print('4. Редактировать данные по оценкам')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        marks = int(input('Введите индекс оценки которую хотите изменить: '))
        mark_new = int(input('Введите оценку: '))
            # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_][marks] = mark_new
            print(f'Для {student} по предмету {class_} исправлена оценка {mark_new}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
        print()
    elif command == 5:
        print('5. Удалить данные по оценкам')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        marks_del = int(input('Введите индекс оценки которую хотите удалить: '))
        # если данные введены верно
        if student in students_marks and class_ in students_marks[student] and marks_del in range(3) :
            # удаляем оценку для ученика по предмету
            marks = marks.pop(marks_del)
            print(f'Для {student} по предмету {class_} удалена оценка {marks}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
        print()
    elif command == 6:
        print('6. Редактировать данные по предметам')
        class_ = input('Введите предмет: ')
        class_new = input('Введите новый предмет: ')
        # если данные введены верно
        if class_ in classes :
            # добавляем новую оценку для ученика по предмету
            classes[classes.index(class_)] = class_new
            for student in students_marks:
                students_marks[student][class_new] = students_marks[student][class_]
            print(f' Предмет {class_} исправлен на {class_new}')
        # неверно введено название предмета
        else:
            print('ОШИБКА: неверное название предмета')
        print()
    elif command == 7:
        print('7. Удалить данные по предметам')
        class_del = input('Введите предмет которую хотите удалить: ')
        # если данные введены верно
        if class_del in classes:
            # удаляем оценку
            classes.remove(class_del)
            for student in students_marks:
                students_marks[student][class_del]
            print(f'Предмет {class_del} удален')
        # неверно введено название предмета
        else:
            print('ОШИБКА: неверное название предмета')
        print()
    elif command == 8:
        print('8. Редактировать данные по ученикам')
        student = input('Введите имя ученика: ')
        student_new = input('Введите новое имя ученика: ')
        # если данные введены верно
        if student in students_marks :
            # добавляем новое имя для ученика
            students[students.index(student)] = student_new
            students_marks[student_new] = students_marks[student]
            print(f' Имя {student} исправлено на {student_new}')
        # неверно введено имя ученика
        else:
            print('ОШИБКА: неверное имя ученика')
        print()
    elif command == 9:
        print('9. Удалить данные по ученикам')
        student_del = input('Введите имя ученика которое хотите удалить: ')
        # если данные введены верно
        if student_del in students:
            # удаляем ученика
            students.remove(student_del)
            print(f'Имя {student_del} удалено')
        # неверно введено имя ученика
        else:
            print('ОШИБКА: неверное имя ученика')
        print()
    elif command == 10:
        print('10. Вывод информации по всем оценкам для ученика')
        student = input('Введите имя ученика: ')
        if student in students_marks:
            for class_ in classes:
                print(f'{class_} - {students_marks[student][class_]}')
        else:
            print('ОШИБКА: неверное имя ученика')
        print()
    elif command == 11:
        print('11. Вывод среднего балла по каждому предмету по определенному ученику')
        student = input('Введите имя ученика: ')
        if student in students_marks:
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету с округлением по правилам математики
                print(f'{class_} - {round(marks_sum // marks_count)}')
        else:
            print('ОШИБКА: неверное имя ученика')
        print()
    elif command == 12:
        print('12. Вывести средний балл по предмету')
        class_ = str(input('Введите название предмета: '))
        if class_ in classes:
            all_marks = []
            # находим сумму оценок по предмету
            for student in students_marks:
                marks = students_marks[student][class_]
                all_marks.extend(marks)
                # выводим средний балл по предмету с округлением по правилам математики
            print(f'{class_} - {round(sum(all_marks) / len(all_marks))}')
        else:
            print('ОШИБКА: неверное название предмета')
        print()
    elif command == 14:
        print('14. Выход из программы')
        break

