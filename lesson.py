coworkers = ['Иванов Олег', 'Сафрнов Андрей', 'Попов Иван', 'Сорокин Владимир', 'Гупанов Кирилл']
print(coworkers[0])
print(coworkers[4])
print()
print(coworkers[0: :1])
print()
print(coworkers[1: :2])
print()
print(len(coworkers))
print()
name=input("Введите имя нового коллеги: ")
coworkers.append(name)
print(len(coworkers))
name = input('Введите имя коллеги: ')
if name in coworkers:
    print('Этот коллега есть в списке')
else:
    print('Такого имени в списке нет')