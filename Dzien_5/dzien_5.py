# # https://drive.google.com/drive/folders/13bYa3t23RVb0HsxO9dWk8ZpnOcPT0L4v?usp=sharing
#
# # funkcje
#
# lst = [1, 2, 3, 4]
# lst.append(10)
# print(lst)
#
#
# # metoda funkcja dzialajaca na konretnym typie danych
#
#
# def some_function():
#     print("Hello")
#
#
# some_function()
#
#
# # print vs return
#
# def function_that_prints():
#     print("I printed")
#
#
# def function_that_returns():
#     return ("I returned")
#
#
# f1 = function_that_prints()
# f2 = function_that_returns()
#
# print(f1)
# print(f2)
#
#
# def passing_function():
#     pass
#
#
# def passing_function2(arg1, arg2):
#     pass
#
#
# passing_function2(arg1=1, arg2=2)
#
#
# # Wielokrotne używanie tego samego kodu
#
# def hallo_function(name):
#     return "Hello and thanks for being here, %s!" % name
#
#
# print(hallo_function("karolina"))
# name = "Maja"
# print(hallo_function(name))
#
# print(hallo_function(name="Karolina"))
#
# students = ["Asia", "Basia", "Kasia", "Patryk", "Piotr"]
# students.sort()
# print(students)
# students.sort(reverse=True)
# print(students)
#
#
# def show_students(students, message):
#     print(message)
#     students.sort()
#     for student in students:
#         print(student)
#
#
# show_students(students=students, message="We are alphabetic!")
#
#
# def get_number_word(number):
#     '''This function takes numerical value and returns a string'''
#     if number == 1:
#         return "one"
#     elif number == 2:
#         return "two"
#     elif number == 3:
#         return "three"
#     elif number == 4:
#         return "four"
#     elif number == 5:
#         return "five"
#     elif number == 6:
#         return "six"
#     elif number == 7:
#         return "seven"
#     elif number == 8:
#         return "eight"
#     elif number == 9:
#         return "nine"
#     elif number == 0:
#         return "zero"
#
#
# print(get_number_word(1))
#
# for i in range(5):
#     print(i, get_number_word(i))
# for i in range(12):
#     print(i, get_number_word(i))
#
#
# def print_num_dict(num):
#     for i in range(num+1):
#         print(i, get_number_word(i))
#
# print_num_dict(10)
#
#
#
# def search(chain, element):
#     for i in chain:
#         if i == element:
#             return "element found", element
#     print("not found ", element)
#
#
# print(search("ala ma kota", "a"))
#
#
# def best_food(food):
#     print("My best food is" , food)
#
# best_food("fries")
#
#
# def best_food_default(food="pizza"):
#     print("My best food is" , food)
#
# best_food_default()
# best_food_default("dykta")
#
# def bonus_counter(salary, proc = 0.1):
#     bonus = salary * proc
#     return bonus
#
#
# print(bonus_counter(5000))
# print(bonus_counter(5000, 0.3))
#
# salary = 1000
# def bonus_counter1(salary, proc = 0.1):
#     bonus = salary * proc
#     return bonus
#
#
# print(bonus_counter1(salary))
#
#
# proc_extra = 10000000000000
# def bonus_counter_local(salary, proc=0.1):
#     proc_extra = 1000
#     bonus = salary * proc + proc_extra
#     return bonus
#
# print(bonus_counter_local(10000))
# print(proc_extra)
#
#
# #interakcje
#
# example = [1,2,3,4,5]
# print(example)
#
# from random import shuffle
# shuffle(example)
# print(example)
#
#
# def shuffle_list(mylist):
#     shuffle(mylist)
#     return mylist
#
# gamelist = ["","0",""]
#
# def player_guess():
#     guess = ""
#     while guess not in ["0","1","2"]:
#         guess = input("pick a cup nuber by index (0,1,2)")
#         return int(guess)
#
# #player_guess()
#
# def check_guess(mylist, guess):
#     if mylist[guess]=="0":
#         print("win")
#     else:
#         print("try agian")
#
# check_guess(shuffle_list(gamelist),player_guess())
#
# print(shuffle_list(gamelist))
# print(shuffle_list(gamelist))
# print(shuffle_list(gamelist))


def fun1(a, b):
    return sum((a, b)) * 0.5


print(fun1(a=5, b=10))


def fun2(a, b, c=0, d=0):
    return sum((a, b, c, d)) * 0.5


print(fun2(4, 5))


def fun3(*args):
    return (sum((args))) * 0.5


print(fun3(1, 2, 3, 4, 5))


def fun4(a, b=0, *c):  # c bedzie z *oznaczało args. Czyli tutaj jeden nazwany, jedne opcjonalny i args
    print(a)
    print(b)
    print(c)


fun4(99, 2, 4)  # args będą drukować się jak tupla, tutaj jednoelementowa


def fun5(a, b=0, **c):  # dwie * oznaczają kwargs
    print(a)
    print(b)
    print(c)


fun5(99, 2, c=4)


def fun6(a, b=0, *c, **d):
    print(a)
    print(b)
    print(c)
    print(d)


fun6(15, 5, 78, d=12)

fun6(15, 5, 78, d=12)
fun6(15, 5, 78, 12)
fun6(15, 5, 78, 12, d=12)


def fun7(*args, **kwargs):
    if "fruit" and "juice" in kwargs:
        print(f"I like {'and'.join(args)} and my favourite fruit is {kwargs['fruit']}")
        print(f" and I have some {kwargs['juice']} juice")
    else:
        print("I do not have what you want")


fun7("schabowy", fruit="ananas", juice="pomaranczowy")


def square(num):
    return num ** 2


num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(map(square, num_list))

print(list(map(square, num_list)))


def str_div(string):
    if len(string) % 2 == 0:
        return "even"
    else:
        return string[0]


names = ["Asia", "Basia", "Kasia", "Patryk", "Piotr"]

print(list(map(str_div, names)))


def div_3(num):
    return num % 3 == 0


num = [0, 7, 8, 9, 10]
print(list(filter(div_3, num)))


def square(num):
    return num ** 2


square_lam = lambda num: num ** 2

print(square_lam(2))
print((lambda s: s[::-1])([9, 10, 11]))

print(list(map(lambda num: num ** 2, num_list)))

print(list(filter(lambda n: n % 2 == 0, num)))
