# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x^2 + 4x + 5 = 0 или x^2 + 5 = 0 или 10x^2 = 0


import random

k = int (input ("Введите пожалуйста значение больще единицы: "))
coefficient = []
for i in range (k):
    coefficient.append (random.randint (0,100))


data = open ('file_for_exercie_4.txt','w')
for i in range (k-1):
    if coefficient[i] != 0:
        data.write (str (coefficient[i]) + 'x^'+ str (k - i - 1) + ' + ')
if coefficient[i-1] != 0:
    data.write (str(coefficient[i-1]))
data.write (' = 0')
data.close()