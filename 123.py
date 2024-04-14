"""Лабораторная работа №2
Написать программу, решающую задачу из 1 лабораторной работы (в соответствии со своим вариантом) со следующими изменениями:
1.Входной файл является обыкновенным (т.е. нет требования на «бесконечность» файла);
2.Распознавание и обработку делать  через регулярные выражения;
3.В вариантах, где есть параметр (например К), допускается его заменить на любое число;
4.Все остальные требования соответствуют варианту задания лабораторной работы №1.

Вариант 16. Четные двоичные числа, не превышающие 819210, в которых встречается не более одной серии из трех подряд идущих нуля. Выводит на экран цифры числа, исключая нули. 
Отдельно выводится прописью номер позиции, с которой начинается эта серия.
"""
import re

with open('7.txt') as file:
    for line in file:
        sl = line.split()
        for num in sl:
            b = num
            if re.fullmatch('^(?!.*000.*000)[01]*0$', b):
                if int(num, 2) <= 8192:
                    print('Число: ',b)
                    pos = b.find('000') + 1
                    if pos == 0:
                        print('В числе нет серии 000')
                    print("Номер позиции с которой начинается серия 000:", pos)
                    b = b.replace('0','')
                    print("Число исключая 0:", b, '\n')
                else:
                    print('Число не подходит под условие\n')
            else:
                print('Число не подходит под условие(четное, не более одной серии из 000 \n')
