import random
numbers = [0] * 20 #список 
unic = [] #список уникальных пар
kolvo = 0 #количество пар, чья сумма меньше заданного пользователем значения.
for i in range(20): #заполнение списка и кортежей рандомными числами
    numbers[i] = tuple(sorted([random.randint(-10, 10) for a in range(4)]))  
for i in numbers: #проверка уникальных пар и добавление к списку
    if numbers.count(i) == 1:
        unic.append(i)
print("Все уникальные пары: ", unic) #вывод уникальных 
b = int(input("Введите целое число: ")) ##ввод Пользователем целого числа
for i in numbers: #колво пар чья сумма меньше b
    kolvo +=(1 if i[0] + i[1] + i[2] + i[3] < b else 0)
print(f"Количество пар, чья сумма < {b} = {kolvo}") #вывод колва
