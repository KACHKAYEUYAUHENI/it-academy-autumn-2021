# Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
# Учитывать только английские буквы.

string_ = input("введите строку")
upper = 0
lower = 0

for i in string_:
    if "a" <= i <= "z":
        lower += 1
    elif "A" <= i <= "Z":
        upper += 1
print("Строчных букв", lower, "Прописных букв", upper)
