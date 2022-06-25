# Zadanie domowe nr 1
# 1. Napisz pętlę, która wydrukuje wszystkie wartości unikalne z listy. Przetestuj na kilku listach.

# listy do testów
list1 = [1, 3, 4, 2, 1, 4, 5]

list2 = ['tak', 'nie bardzo', 55, 11, True,'nie bardzo', 55]

lista_unique = []

for i in list1:
    if i not in lista_unique:
        lista_unique.append(i)

print(lista_unique)

lista_unique = []

for i in list2:
    if i not in lista_unique:
        lista_unique.append(i)

print(lista_unique)

# 2. Proszę, używając pętli, wypisać co trzecią liczbę z zakresu 1 do 100

for i in range(0, 11, 3):
    print(i)

# 3. Za pomoca petli wydrukuj nastepujacy wzorzec:
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

# 1 wersja


for i in range(1, 10):
    for j in range(1, i + 1):
        print(i, end="")
    print()

# 2 wersja


k = 1
while k <= 9:
    j = 1
    while j <= k:
        print(k, end="")
        j += 1
    print()
    k += 1

# 4. Napisz pętlę, która wyświetli, po podaniu liczby, tabliczkę mnożenia.
# Przykładowo: Wprowadź liczbę:
# 6 6x1 = 6
# 6x2 = 12
# 6x3 = 18
# 6x4 = 24
# 6x5 = 30
# 6x6 = 36
# 6x7 = 42
# 6x8 = 48
# 6x9 = 54
# 6x10 = 60

number = int(input("Wprowadz liczbe, dla ktorej wyświetlisz tabliczkę mnożenia : "))
# Uzywajac petli iterujemy sie przez liczby 1-10 za kazdym razem mnazac numer przez kolejna z niach.
# Wszystko ubieramy w elegancki print
print("Wprowadzona liczba: ", number)
for count in range(1, 11):
    print(number, 'x', count, '=', number * count)

# 5. Utwórz słownik: słownik = {"Ania":1200, "Ola":1300, "Arek":3000}
# Zaktualizuj dla niego wartość Ania:200, Arek:100
# Sprawdź czy istnieje w słowniku „Ola”
# Sprawdź czy ktoś zarabia 200 zł
# Policz elementy słownika
# Wyczyść słownik.

dict_name_val = {"Ania": 1200, "Ola": 1300, "Arek": 3000}
print("Przed aktualizacją: {}".format(dict_name_val))

# Aktualizacja wartości
dict_name_val.update({"Ania": 200, "Arek": 100})
print("Po aktualizacji: {}".format(dict_name_val))
# Czy Ola występuje w słowniku
name = "Ola"
if name in dict_name_val:
    print("Imię {} ISTNIEJE w słowniku.".format(name.title()))
else:
    print("Imię {} NIE ISTNIEJE w słowniku.".format(name.title()))
# Sprawdzenie kto zarabia 200

val = 200
name_val = []
dict_name_val.update({"Roman": 200})  # dodanie imienia
print("Rozszerzony słownik - dodatkowa osoba Roman: {}".format(dict_name_val))
for key, value in dict_name_val.items():
    if value == val:
        name_val.append(key)
    else:
        continue
if name_val:
    print("1. Osoby zarabiające {} zł to: ".format(val) + ", ".join(name_val))
else:
    print("1. Brak w słowniku osób zarabiających {} zł".format(val))

# Liczba elementów w słowniku
print("Ilość elementów w słowniku: {}".format(len(dict_name_val)))

# wyczyszczenie słownika

dict_name_val.clear()

# 6. *Biorąc pod uwagę wartości listy i listę kluczy, przekonwertuj te wartości na pary klucz-wartość w postaci listy słowników.
value_list = ["A", 8, "is", 3, "B", 7, "C", 1, "D", 3]
key_list = ["name", "number"]
# Oznacza to, że output ma wyglądać w ten sposób:
# [{'name': 'A', 'number': 8},
# {'name': 'is', 'number': 3},
# {'name': 'B', 'number': 7},
# {'name': 'C', 'number': 1},
# {'name': 'D', 'number': 3}]

dicts = []

for i in range(0, len(value_list), 2):
    dicts.append({str(key_list[0]): value_list[i], str(key_list[1]): value_list[i + 1]})

print(dicts)
