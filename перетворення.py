x = input("Введи ціле число: ")
y = input("Введи десяткове число: ")

print("Типи до:", type(x), type(y))  # обидва str
x = int(x)
y = float(y)
print("Типи після:", type(x), type(y))
print("Сума:", x + y)
