import numpy as np
import pandas as pd


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


print(Divisors(1331))
