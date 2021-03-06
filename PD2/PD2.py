import numpy as np
import datetime as dt


# ----------------------------------------------------------------------------------------------------------------
# 1. Napisz funkcję, która wypisze liczby od 1 do 100, przy czym liczby podzielne przez 3
# zastąp słowem ‘Fizz’, liczby podzielne przez 5, zastąp słowem ‘Buzz’, natomiast liczby
# podzielne i przez 3 i przez 5 zastąp słowem ‘FizzBuzz’.
# A w rezultacie, powinniśmy otrzymać – 1, 2, Fizz, 4, Buzz, 6, 7, 8, Fizz, Buzz, 11, Fizz, 13,
# 14, FizzBuzz, 16 itd

def FizzBuzz():
    v = []
    for i in range(101):
        if i % 15 == 0:
            v.append('FizzBuzz')
        elif i % 3 == 0:
            v.append('Fizz')
        elif i % 5 == 0:
            v.append('Buzz')
        else:
            v.append(i)
    return v


print(FizzBuzz())


# ----------------------------------------------------------------------------------------------------------------------
# 2. Napisz funkcję, która będzie wymieniała wszystkie dzielniki danej liczby

def Divisors(n):
    divisors = []
    stop = int(np.sqrt(n))
    for i in range(1, stop):
        if n % i == 0:
            divisors.append(i)
            divisors.append(int(n / i))
    divisors.sort()
    return divisors


print(Divisors(3600))


# ------------------------------------------------------------------------------------------------------------------------
# 3. Napisz funkcję, która będzie podawała wiek danej osoby, jesli podany zostanie rok.

# Sprawdzenie czy rok jest przestępny
def Leap_year(year):
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        return True
    else:
        return False


def Age(y, m, d):
    birth_date = dt.date(y, m, d)
    actual_date = dt.date.today()
    if (birth_date.month == 2
            and birth_date.day == 29
            and Leap_year(actual_date.year) == False
            and actual_date.month == 2
            and actual_date.day == 28):  # wyjatek dla urodzonego 29.02 - w latach nieprzestepnych przyjmujemy 28.02 jako dzien urodzin
        age = actual_date.year - birth_date.year
    elif birth_date.month > actual_date.month or (
            birth_date.month == actual_date.month and birth_date.day > actual_date.day):
        age = actual_date.year - birth_date.year - 1
    else:
        age = actual_date.year - birth_date.year

    return age


print(Age(1974, 6, 24))


# 4. Napisz funkcję, która będzie szukala podanego znaku w ciagu znaków

def Search(text):
    char = str(input('Podaj znak:'))
    if char in text:
        return True
    else:
        return False


text = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print(Search(text))


# -----------------------------------------------------------------------------------------------------------------------
# 5. Napisz funkcję, która będzie liczyła ile razy w łańcuchu znaków występują samogłoski

def Vowels(text):
    vowels = ['A', 'Ą', 'E', 'Ę', 'I', 'O', 'Ó', 'U', 'Y']
    counter = 0
    for character in text:
        if character.upper() in vowels:
            counter += 1

    return counter


test_text = 'Napisz funkcję, która będzie liczyła ile razy w łańcuchu znaków występują samogłoski'

print(Vowels(test_text))


# -----------------------------------------------------------------------------------------------------------------------
# 1. Napisz 3 klasy, które prezentują zależność Czlowiek -> Dziecko -> Przedszkolak
# Czlowiek niech ma imie, wiek i plec oraz 2 dowolne metody
# Dziecko niech ma cechy klasy nadrzednej oraz ulubioną zabawkę
# Przedszkolak musi mieć podana grupe, do ktorej uczeszcza
# Każda klasa musi posiadać metodę 'show_info' i konstruktor

class Czlowiek():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def drink(self, drink):
        print('{} drinks {}'.format(self.name, drink))

    def sleep(self):
        print('{} sleeps'.format(self.name))

    def show_info(self):
        print("My name is {}".format(self.name))
        print("I am {} years old".format(self.age))


class Dziecko(Czlowiek):
    def __init__(self, name, age, sex, fav_toy):
        super().__init__(name, age, sex)
        self.fav_toy = fav_toy

    def show_info(self):
        super().show_info()
        print("{} is my favourite toy".format(self.fav_toy))


class Przedszkolak(Dziecko):
    def __init__(self, name, age, sex, fav_toy, group):
        super().__init__(name, age, sex, fav_toy)
        self.group = group

    def show_info(self):
        super().show_info()
        print("{} is my group".format(self.group))


human = Czlowiek(name="Tomasz", age=42, sex="M")
kid = Dziecko(name="Ania", age=8, sex="F", fav_toy="Dollhause")
kid2 = Przedszkolak(name="Michał", age=5, sex="M", fav_toy="Teddy bear", group="Smurfs")

human.show_info()
human.sleep()
human.drink("water")

kid.show_info()
kid.drink("juice")

kid2.show_info()
kid2.sleep()


# 2. (*) Napisz 3 klasy, ktore beda obrazowaly zaleznosc (Auto, Budynek) -->Kamper, kazda
# klasa musi miec minimum 2 metody. Jest to przykład multiple inheritance, którego nie
# mieliśmy na zajęciach.


class Auto():
    def __init__(self, brand):
        self.brand = brand

    def ride(self):
        print("The {} rides".format(self.brand))

    def refuel(self):
        print("The {} has full tank".format(self.brand))


class Budynek():
    def __init__(self, places):
        self.places = places

    def bedroom(self):
        print("It has {} places in bedroom".format(self.places))

    def clean(self):
        print("The bedroom is cleaned")


class Kamper(Auto, Budynek):
    def __init__(self, brand, places):
        Auto.__init__(self, brand)
        Budynek.__init__(self, places)


kamp = Kamper(brand='BMW', places=4)

kamp.ride()
kamp.refuel()
kamp.bedroom()
kamp.clean()

