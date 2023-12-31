# Homework 8 - Vladyslav

""" Подключение функций """
from random import randint # импортирую функцию randint из библиотеки random

""" Создание списков """
list1 = [randint(0, 100) for i in range(1000)] # создаю случайно сгенерированный список
print(list1[0:10]) # вывожу первые 10 элементов списка до сортировки в консоль
list1_copy = sorted(list1.copy()) # создаю сортированную копию списка

""" Процедура сортировки расческой """
def comb_sort(list): # создаю процедуру сортировки
    sorting = True # разрешаю сортировку
    step = len(list) # начальный шаг = длина списка
    
    while sorting == True: # сортировка пока сортируеться
        step = step / 1.3 # делю шаг на это число, которое нашли самым эффективным при экспериментах с другими массивами
        # если шаг дошел до 1, он превращаеться в сортировку пузырьком, проходит один раз, и заканчивается
        intStep = int(step) # делаю копию числа без точек
        
        for index in range(0, len(list) - intStep): # прохожу через индексы
                if list[index] > list[index+intStep]:  # если первый индекс больше второго
                    list[index], list[index+intStep] = list[index+intStep], list[index] # поменять местами
        
        if step <= 1: # если шаг дошел до 1
            sorting = False # закончить сортировку

""" Вызов сортировки """
comb_sort(list1) # вызываю процедуру сортировки

""" Проверка """
if list1 != list1_copy: # делаю проверку что список правильно отсортирован
    for i in range(len(list1)-1): # прохожу по индексам
        if list1[i] != list1_copy[i]: # сравниваю индекс моей сортировки, и встроенной
            print(list1[i], list1_copy[i]) # вывожу разницу
    raise Exception("NOT SORTED RIGHT") # вызываю ошибку 

""" Вывод """
print(list1[0:10]) # вывожу первые 10 символов сортированного списка