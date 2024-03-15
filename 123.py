import re
with open('7.txt') as file:
    for line in file:
        numbers = re.findall(r'\b\d+\b', line)
        if not numbers:
            print('Файл закончился')
            break
        for num_str in numbers:
            num = int(num_str, 2) if re.match(r'^0b[01]+$', num_str) else int(num_str)
            if num <= 8192 and num % 2 == 0:
                b = bin(abs(num))[2:]
                b = re.sub(r'000', '*', b)
                if b.count("*") == 1:
                    pos = b.find('*') + 1
                    b = b.replace("*", "")
                    print(b, pos)


#111001 7
#111 4
#1110010 3
#1010 4
#100 2
#1010110 6
#111 4
#1111101 8
#Файл закончился