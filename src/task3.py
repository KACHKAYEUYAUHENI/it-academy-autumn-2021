# Tuple practice
# Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
# Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
# Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
# Создайте кортеж из одного элемента,
# чтобы при итерировании по этому элементы последовательно выводились значения 1, 2, 3.
# Убедитесь что len() исходного кортежа возвращает 1.

lst1 = ["a", "b", "c"]
tpl1 = tuple(lst1)

tpl2 = ('a', "b", "c")
lst2 = list(tpl2)

a, b, c = "a", 2, "python"

tpl3 = ("1, 2, 3", )
for i in tpl3:
    print(i)
print(len(tpl3))
