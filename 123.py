import re
with open('7.txt') as file:
    for line in file:
        sl = line.split()
        for num in sl:
            if all('0' <= num_str <= '1' for num_str in num):
                if int(num,2) <= 8192 and int(num,2) % 2 == 0:
                    if re.fullmatch('[0-1]*000[0-1]*', b):
                        b = re.sub(r'000', '*', b)
                        if b.count("*") == 1:
                            pos = b.find('*') + 1
                            b = b.replace("*", "")
                            print("Число исключая серию 000:", b)
                            print("Номер позиции ", pos)
            else:
                print('Неверный формат числа')
