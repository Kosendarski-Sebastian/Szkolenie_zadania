#1. Z poniższej listy, z użyciem list comprehension, usuń elementy ktore nie sa 30-stka.
list1 = [5, 20, 15, 30, 25, 50, 90, 30]
list1_out = [element for element in list1 if element != 30]
print(list1_out)

#2. Mając poniższą listę (list2) zmodyfikujac ja tak, zeby uzyskac:
#[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
list2 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list2[2][2].append(7000)
print(list2)

# 3. Z podanych niżej list utwórz:
#['My', 'name', 'is', 'Kelly']
#Użyj funkcji zip().

list5 = ["M", "na", "i", "Ke"]
list6 = ["y", "me", "s", "lly"]

