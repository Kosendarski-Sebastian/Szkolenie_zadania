#1. Napisz funkcję o nazwie show_numbers, która przyjmuje parametr o nazwie limit.
# Powinien wydrukować wszystkie liczby od 0 do limitu z etykietą, aby zidentyfikować
# liczby parzyste i nieparzyste. Na przykład, jeśli limit wynosi 3,
# powinien wydrukować: 0 EVEN 1 ODD 2 EVEN 3 ODD
import math


def show_numbers(limit):
    for i in range(limit+1):
        if i %2 ==0:
            print(i, "EVEN")
        else:
            print(i, "ODD")

limit = 30
show_numbers(limit)
#----------------------------------------------------------------

#2. Napisz funkcję, która wypisuje wszystkie liczby pierwsze od 0 do limitu, gdzie limit jest parametrem.

lim = 100

def primes(num):
    for i in range(2,num+1):
        counter = 0
        for j in range(0, math.ceil(math.sqrt(i))):
            if i%2==0:
                counter +=1
            else:
                return
        if counter == 0:
            print(i)
        else:
            return

primes(10)







