string = "Lorem ipsum dolor sit amet, consectetur adipisicing elit."

# Поділ рядка поелементний, при цьому створюється список
print(string.split())

print(string.strip()) #Видалення пробільних символів на початку і в кінці рядка
print(string.count('s')) #рахує кількість елементу в дужках
print(string.replace('Lorem', 'LOREM')) #заміняє перший елемент на другий

print(str(len(string)).isdigit()) #перевіряє чи складається рядок з цифр

print(string.title()) #кожне слово з великої букви
print(string.capitalize()) #лише перший симол рядка в верхній регістр
print(string.lower()) #нижній регістр
print(string.upper()) #верхній регістр

print(string.center(100, '+')) #Повертає відцентрований рядок, по краях якого стоїть символ fill (пробіл за замовчуванням)

print(string.startswith('L'))
print(string.endswith('.'))

print('string'.isalpha()) #чи складається рядок з літер
print(string.casefold()) #перетворює всі символи на нижній регістр і видаляє відмінності регістрів, що важливо для Unicode
