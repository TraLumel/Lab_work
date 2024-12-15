#Задание 1: Импорт стандартных модулей
import math
import datetime 
print(math.sqrt(int(input('Введите число '))))
current_datetime = datetime.datetime.now()
print(current_datetime)

#Задание 2: Создание и использование собственного модуля
import my_module
a=input('Введите 1 число ')
b=input('Введите 2 число ')
print (my_module.sum(a,b))

#Задание 3: Создание и использование пакетов
from my_package import number, string
print(string.lesenka('Привет, меня зовут Олег.'))
print (number.proizvedenie(6,23))