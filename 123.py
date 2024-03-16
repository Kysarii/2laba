import re
file = open('7.txt')
while True:
    a = file.readline().split()
    if not a:
        print('Файл закончился')
        break
    for num in a:
        if all('0' <= num_str <= '1' for num_str in num):
            if int(num,2) <= 8192 and int(num,2) % 2 == 0:
                if re.fullmatch('[0-1]*000[0-1]*', num):
                    b = re.sub(r'000', '*', num)
                    if b.count("*") == 1:
                        pos = b.find('*') + 1
                        b = b.replace("*", "")
                        print("Число исключая серию 000:", b)
                        print("Номер позиции ", pos)
        else:
            print('Неверный формат числа')
