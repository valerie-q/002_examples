#Завдання 1 — Типи даних

a = 10
b = 3.14
c = "Python"
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))


#Завдання 2 — Калькулятор

x = float(input("Введіть перше число: "))
y = float(input("Введіть друге число: "))

print("Сума:", x + y)
print("Різниця:", x - y)
print("Добуток:", x * y)
print("Частка:", x / y)
print("Остача:", x % y)


#Завдання 3 – привітання з користувачем

name = input("Введи своє ім'я: ")
color = input("Введи свій улюблений колір: ")

print(f"Привіт, {name}! Твій улюблений колір — {color}.")




#Завдання 4 -  вік

birth_year = int(input("Введи рік народження: "))

current_year = 2026
age = current_year - birth_year

print("Тобі приблизно", age, "років.")



#Завдання 5 – Подвоювач
word = input("Введи слово: ")

print(word * 2)



#Завдання 6 - Середнє значення 

a = float(input("Введи першу оцінку: "))
b = float(input("Введи другу оцінку: "))
c = float(input("Введи третю оцінку: "))

average = (a + b + c) / 3

print("Середнє значення:", average)
#або print("Середнє значення:", round(average, 2))



#Завдання 7 — Перевірка проміжку

x = int(input("Введіть число: "))
print(10 <= x <= 20)



#Завдання 8 — Площа і периметр прямокутника

length = float(input("Введіть довжину: "))
width = float(input("Введіть ширину: "))

area = length * width
perimeter = 2 * (length + width)

print(f"Площа: {area} см², Периметр: {perimeter} см")


#Завдання 9 - 🧁 Печиво для друзів

n = int(input("Скільки є печив? "))
k = int(input("Скільки друзів? "))

cookies_per_friend = n // k
remaining = n % k

print("Кожен отримає:", cookies_per_friend)
print("Залишиться:", remaining)



#Завдання 10 - 🧩 Остання цифра

n = int(input("Введіть ціле число: "))

last_digit = n % 10

print("Остання цифра:", last_digit)



#Завдання 11 - 💡 Персональний банер

name = input("Введіть ім'я: ")
hobby = input("Введіть хобі: ")

line1 = "* Мене звати " + name + " *"
line2 = "* Люблю " + hobby + " *"

width = max(len(line1), len(line2))
border = "*" * width

print(border)
print(line1)
print(line2)
print(border)


words = sentence.split()
print("Кількість слів:", len(words))



#Завдання 15 - км в милі
kilometers = float(input("Enter distance in kilometers: "))
# Conversion factor: 1 kilometer = 0.621371 miles
conversion_factor = 0.621371
miles = kilometers * conversion_factor
print(f"{kilometers} kilometers is equal to {miles} miles")

