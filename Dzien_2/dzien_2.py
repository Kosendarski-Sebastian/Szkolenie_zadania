# num = float(input("Dej liczbe:"))
# foo = 2.5
# print(foo)
#
# v_1 = round(foo)  # zaokrągla w dół przy 0.5)
# print(v_1)
#
# foo_1 = 'Monty Python'
# print(foo_1)
# print(type(foo_1))
# # foo_2 =  'Monty Python's Flying Circus'
# foo_3 = "Monty Python's Flying Circus"  # zapis prawidłowy
# foo_4 = """Monty
#             Python"""
# print(foo_3)
# print(foo_4)
# foo_5 = "Monty \n Python"
# print(foo_5)
#
# foo_6 = "monty python"
# print(foo_6.capitalize()) # z wielkiej litery
# print(foo_6.upper()) # zamiana na wielkie
# print(foo_1.lower()) # zamiana na male
#
# #po kropce uzywane są metody
#
#
# #indeksowanie
#
# person = "Sebastian Kosendarski"
# print(person[0]) #wybor elementu - nawiasy kwadratowe zaczynamy od 0
# print(person[-1]) # ale od końca -1, -2,-3,...
# # START:STOP:STEP
# print(person[:5]) # do elementu o nr x bez elementu x (bez startu)
# print(person[0:5]) # do elementu o nr x bez elementu x (bez startu)
# print(person[0:5:1]) # do elementu o nr x bez elementu x (bez startu)
#
# print(person[:9])
# print(person[10:])
# print(person[:21])
#
# print(person[:-3])
# print(person[0::2])
#
#
# name = "Sebastian"
# last_name = "Kosendarski"
# print(name + " " + last_name)
# print(2*name)
#
#
# # var1="6"
# # var2="9"
# # print(int(var1)*int(var2))
# # print(int(input("Submit the number of orders:")))
# # a = int(input("Submit the number of orders:"))
#
# # num1 = int(input())
# # num2 = int(input())
# print("liczba ujemna")
# if num > 0 or num==0:
#     print("liczba jest niuejemna")
#
# else:
#     if num > 0:
#         print("liczba jest dodatnia")
#     elif num==0:
#         print("ziobro")
#     else:
#         print("liczba ujemna")
# # num3 = num1 - num2
# # print(num3)
#
#
# #instrukcje warunkowe
#
# x=10
# if x > 10:
#     print("x>10")
#
#

# generator

#
# gen = range(-10, 10, 1)
# print(list(gen))  # w ramach standardowych bibliotek tylko integer


####Pętle

for i in range(5):
    print(i)

students = ["Ania", "Zosia", "Marysia"]
for student in students:
    print(student)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for element in list_of_lists:
    print(element[0])


empty_list=[]
for i in students:
    empty_list.append(i)
print(empty_list)