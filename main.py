s = input("За какое количество дней вы хотите ввести температуру? ")
ok = False
if s.isdigit():
    if int(s) < 1:
        print("Ошибка! Введено число, которое меньше 1.")
        print("Завершение работы программы.")
        exit()
else:
    print("Ошибка! Введённая строка не является целым числом.")
    print("Завершение работы программы.")
    exit()
n = int(s)
print(n)
temp = []
for i in range(n):
    s = input()
    print(s)
    # temp.append()