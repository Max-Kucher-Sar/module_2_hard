password = int(input('Введите число: '))
str_ = []

for i in range(1, password + 1):
    for j in range(i + 1, password + 1):
        if password % (i + j) == 0:
            str_.append(str(i) + str(j))

print('Число: ', password)
print('Пароль: ', *str_, sep='')
