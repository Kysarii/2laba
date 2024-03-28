import re
with open('7.txt') as file:
    for line in file:
        sl = line.split()
        for num in sl:
            b = num
            if all('0' <= num_str <= '1' for num_str in num):
                if int(num,2) <= 8192 and int(num,2) % 2 == 0:
                    if re.fullmatch('^(?!.*000.*000)[01]+$', b):
                        print("Число:", b)
                        for i in re.finditer('000', b):
                            index = i.start()
                            print("Номер позиции с которой начинается серия 000:", index)
                        b = b.replace("0", "")
                        print("Число исключая 0:", b)
                        print()
                    else:
                        print('В числе 2 или больше серии из 000')
                        print()
                else:
                    print('Число не подходит под условие')
                    print()
            else:
                print('Неверный формат числа')
                print()
