# Числа у десятковій системі числення
decimal_1 = 8
decimal_2 = 42
decimal_3 = -3
decimal_4 = 258028365723567230582038

print(decimal_1)
print(decimal_2)
print(decimal_3)
print(decimal_4)
# пусто print для перенесення рядка
print()

# Побудова цілого числа з іншого значення
string = "15"
number = string
print(number)
print(string)
print(number + str(5))
# string + 5 -- помилка TypeError: can only concatenate str (not "int") to str
print(int(number) + 5)
print(number * 5)
print(int(number) * 5)
