# 1. Napisz pętlę, która wydrukuje wszystkie wartości unikalne z listy.
# Przetestuj na kilku listach.

list1 = [1, 2, 3, 4, 5, 5, 5, "a", "b", "b"]
list1_out = []
for element in list1:
    if element not in list1_out:
        list1_out.append(element)
print(list1_out)

# ---------------------------------------------------------------------------------------------------
# 2. Proszę, używając pętli, wypisać co trzecią liczbę z zakresu 1 do 100

print([i for i in range(101) if i % 3 == 1])

# #3. Za pomoca petli wydrukuj nastepujacy wzorzec:
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

for i in range(10):
    print(i * str(i))

# ---------------------------------------------------------------------------------------------------------
# 4. Napisz pętlę, która wyświetli, po podaniu liczby, tabliczkę mnożenia.
# Przykładowo:
# Wprowadź liczbę: 6
# 6x1 = 6
# 6x2 = 12
# 6x3 = 18
# 6x4 = 24
# 6x5 = 30
# 6x6 = 36
# 6x7 = 42
# 6x8 = 48

num = int(input("Wprowadź liczbę: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# --------------------------------------------------------------------------------------------------------------
# 5. Utwórz słownik: słownik = {"Ania":1200, "Ola":1300, "Arek":3000}
# Zaktualizuj dla niego wartość Ania:200, Arek:100
# Sprawdź czy istnieje w słowniku „Ola”
# Sprawdź czy ktoś zarabia 200 zł
# Policz elementy słownika
# Wyczyść słownik.

dict1 = {"Ania": 1200, "Ola": 1300, "Arek": 3000}
print(dict1)
dict1.update({"Ania": 200,
              "Arek": 100})
print("Czy w słowniku istnieje Ola: ", "Ola" in dict1.keys())
print("Czy w ktoś zarabia 200: ", 200 in dict1.values())
print("Słownik ma ", len(dict1), "elementy")
dict1.clear()
print(dict1)

# ----------------------------------------------------------------------------------------------------------------
# 6. *Biorąc pod uwagę wartości listy i listę kluczy, przekonwertuj te wartości na pary
# klucz-wartość w postaci listy słowników.
# value_list = ["A", 8, "is", 3, "B", 7, "C", 1, "D", 3]
# key_list = ["name", "number"]
# Oznacza to, że output ma wyglądać w ten sposób: [{'name': 'A', 'number': 8}, {'name': 'is',
# 'number': 3}, {'name': 'B', 'number': 7}, {'name': 'C', 'number': 1}, {'name': 'D', 'number': 3}]

value_list = ["A", 8, "is", 3, "B", 7, "C", 1, "D", 3]
key_list = ["name", "number"]
dict_list = []

for i in range(int(len(value_list) / 2)):
    temp_dict = {key_list[0]: value_list[2 * i], key_list[1]: value_list[2 * i + 1]}
    dict_list.append(temp_dict)

print(dict_list)
