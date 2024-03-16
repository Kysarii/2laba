import re
file = open('7.txt')
while True:
    a = file.readline().split()
    if not a:
        print('Файл закончился')
        break
    for num_str in a:
        if int(num_str) == int((bin(abs(int(num_str)))[2:])):
            num = int(num_str, 2)
        else:
            num = int(num_str)
        if num <= 8192 and num % 2 == 0:
            b = str(bin(abs(num))[2:])
            if re.fullmatch('[0-1]*000[0-1]*', b):
                b = re.sub(r'000', '*', b)
                if b.count("*") == 1:
                    pos = b.find('*') + 1
                    b = b.replace("*", "")
                    print("Число исключая серию 000:", b)
                    print("Номер позиции ", pos)
