students = ["Ania", "Zosia", "Marysia"]

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

empty_list = []

# zagnieżdzenie pętli
empty_list1 = []
for list1 in list_of_lists:
    for element in list1:
        empty_list1.append(element)

print(empty_list1)

gender = ["Female", "Female", "Female", "Male", "Male", "Male"]
age = [75, 45, 14, 1, 45, 4]
survived_gender = []
survived_age = []
for person in range(len(gender)):  # szukamy po indeksie a nie elemencie
    if gender[person] == "Female":
        survived_gender.append("Survived")
    else:
        survived_gender.append("Died")

print(survived_gender)
for person in range(len(age)):  # szukamy po indeksie a nie elemencie
    if age[person] <= 40:
        survived_age.append("Survived")
    else:
        survived_age.append("Died")

print(survived_age)

# pętla while

variable1 = 1

while variable1 < 7:
    print("variable1 = ", variable1)
    print("variable1**3 = ", variable1 ** 3)
    variable1 = variable1 + 1

variable2 = 1

while variable2 < 7:
    variable2 = variable2 + 1
    print("variable2 = ", variable2)
    print("variable2**3 = ", variable2 ** 3)

print("at the end varialbe2 =", variable2)

# break i continue

for i in range(100):
    print(i)
    if i >= 7:
        break
print("I am outside the loop")

names = ["Rose", "Jack", "Nina", "Max", "Phill"]

for name in names:
    print(f"Hallo, {name}")
    if name == "Nina":
        break
print("I found Nina")

for name in names:
    if name == "Nina":
        continue
    print(f"Hallo, {name}")

print("I am outside the loop")

for i in range(10):
    if i > 4:
        print("the end")
        continue
    elif i < 7:
        print(i)

bank_ror = [58000, -880, -100, 0, 60, 5, 9000, -7894]

for saldo in bank_ror:
    if saldo <= 0:
        continue
    print(saldo)

for i in range(11):
    if i == 7:
        continue
    print(f"the number is {i}")

i = 0
while i <= 10:
    if i == 7:
        i += 1
        continue
    print(f"the number is {i}")
    i += 1

# list comprehension
# najpierw operacja na kolekcji, potem zakres


res = []
for i in range(11):  # 2 (zakres)
    x = 10 * i  # 1 tak zaczynamy list comp (intrukcja)
    res.append(x)  # 3 (miejsce na if-a
print(res)

print([10 * i for i in range(11) if i % 2 == 0])

# kolekcje


fruits = ["apple", "cherry", "bananna"]
print(fruits)
print(type(fruits))

mixed_fruits = [65, True, "apple", 3.14, 2 >= 4]
print(mixed_fruits)
print(type(mixed_fruits))

mixed_fruits.append("pineaplle")
print(mixed_fruits)

mixed_fruits.extend(["orange", "lemon"])
print(mixed_fruits)

mixed_fruits.insert(2, "watermelon")
print(mixed_fruits)

mixed_fruits.pop()
print(mixed_fruits)

mixed_fruits.pop(3)
print(mixed_fruits)

mixed_fruits.reverse()
print(mixed_fruits)

mixed_numbers = [2, 34, 67, 123, 12, 1]
mixed_numbers.sort()
print(mixed_numbers)
mixed_numbers.sort(reverse=True)
print(mixed_numbers)
print(sum(mixed_numbers))
print(min(mixed_numbers))
print(max(mixed_numbers))

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list_of_lists)
# krotka

fruits_tuple = ("apple", "cherry", "bananna")
print(fruits_tuple)
print(type(fruits_tuple))

# zmiana stanu pamięci

print(mixed_fruits)
mixed_fruits[0] = 10
print(mixed_fruits)
#
# print(fruits_tuple)
# fruits_tuple[0] = 10
# print(fruits_tuple)

new_list = list(fruits_tuple)
print(new_list)
new_tuple = ("apple", "cherry", "bananna", "potato")
print(new_tuple)

print(new_tuple + ("potato",)) # przecinek musieć być
fruit = "strawberry"
new_tuple2 = ("apple", "cherry", "bananna", "potato", fruit)
print(new_tuple2)


numeric_tuple = (58000, -880, -100, 0, 60, 5, 9000, -7894)
print(sum(numeric_tuple) / len(numeric_tuple))

dict_person = { "name": "Thomas Anderson",
                "gender" : "male",
                "age": 34,
                "married": True}
print(dict_person.values())
print(dict_person.keys())
print(dict_person["age"])
dict_person["adress"]= "Ship Nebuchadnezzar"
print(dict_person)
dict_person.update({"country": "USA", "education": "MIT"})
print(dict_person)


dict1 = {"name": "Tom", "name":"Larry"}
print(dict1)

dict2 = {"name": "Tom", "name": "Tom"}
print(dict2)


languages1 = {"R", "Java", "Python"}
languages2 = {"R", "Java", "Python", "R"}

print(languages1)
print(languages2)
languages1.add("C#")
print(languages1)

languages_frozen = frozenset(["R", "Java", "Python"])
print(languages_frozen)
print(type(languages_frozen))