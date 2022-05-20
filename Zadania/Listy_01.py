# 1. Z poniższej listy, z użyciem list comprehension, usuń elementy ktore nie sa 30-stka.
list1 = [5, 20, 15, 30, 25, 50, 90, 30]
out1 = [element for element in list1 if element != 30]
print(out1)

# 2. Mając poniższą listę (list2) zmodyfikujac ja tak, zeby uzyskac:
# [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
list2 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
out2 = list2[:]
print(list2)
out2[2][2].append(7000)
print(out2)

# 3. Z podanych niżej list utwórz:
# ['My', 'name', 'is', 'Kelly']
# Użyj funkcji zip().

list5 = ["M", "na", "i", "Ke"]
list6 = ["y", "me", "s", "lly"]
out3 = [i + j for i, j in zip(list5, list6)]
print(out3)

# 4. Majac ponizsza liste, wyczysc ja ze stringow (z uzyciem dowolnej metody) i podaj:
# - jej maximum
# - minimum
# - srednia
# - mediane
list7 = [100, 200, 300, 400, 'str', 'ciastka', 'groszki']
list7_num = [element for element in list7 if type(element)== int]
list7_num.sort()
print(list7_num)
print(max(list7_num))
print(min(list7_num))
print(sum(list7_num)/len(list7_num))

median = float()

print(len(list7_num)/2)
#
# if len(list7_num) == 0 :
#     print("Brak wartosci liczbowych")
# elif len(list7_num) % 2 == 1:
#     n = (list7_num[0] + list7_num[-1]) / 2
#     median = list7_num[n]
#     print(median)
# else:
#     median = (list7_num[len(list7_num)/2]+ list7_num[len(list7_num)/2 -1])/2
#     print(median)
