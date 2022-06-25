import numpy as np
import pandas as pd
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
            and actual_date.day == 28):
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
