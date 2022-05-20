x = 5  # komentarz - zaalokowana zmienna
print(x)
x = 7
print(x)

# to nie jest tekst - [ctrl + /] skrót do kometarza
"""tekst przykładowy docstring, służy do dokumentacji"""

my_favourite_color = 'yellow'  #
print(my_favourite_color)

color1, color2, color3 = 'red', 'orange', 'blue'
print(color1)
print(color2)
print(color3)
color4 = color5 = color6 = 'pink'
print(color4)
print(color5)
print(color6)

counter = 10  # integer
counter = counter + 1
print(counter)

counter += 1  # counter = counter + 1
print(counter)

### Deklarowanie zmiennych

musketeers_3 = ['Athos', 'Aramis', 'Portos']
print(musketeers_3)

# zmienne deklarujemy z małej litery, przy deklarowaniu class uzwamy dużych
# nie zaczynamy od liczb, nie zawiera spacji, znakow specjalnych
# nie nazywamy zmiennych tak jak jakiś inny element języka

### Typy zmiennych
# INT - liczba całkowita
a_variable = 23
print(a_variable)
print(type(a_variable))
###FLOAT
b_variable = 43.25
print(b_variable)
print(type(b_variable))
c_variable = 43.00  # wymusilismy float
print(c_variable)
print(type(c_variable))
# BOOLEAN - true/false
is_today_saturday = True
is_today_wednesday = False
print(is_today_saturday)
print(is_today_wednesday)

###STRING
'tekst'
"tekst"
print('tekst' == "tekst")  # [ctrl + alt + L ] autoformatowanie, == porównanie

###operacje matematyczne
print(5 + 3)
print(type(5 + 3))

print(5000 / 3)
print(5 / 3)
print(type(5 / 3))
print(3 / 3)
print(type(3 / 3))

print(3 * 3)
print(type(3 * 3))

print(3 + 3)
print('3' + '3')
print(type('3' + '3'))

print("hello world")

# script_input = input()
# print(script_input)

print(True and False)
print(True and True)
print(False and False)
print(True or False)
print(True or True)
print(False or False)

print(2 and True)

print(type(1) == type(1.0))
print(True == 1)
print(True == 2)
print(False == 0)

print(1 < 2)
print(1 > 2)
print(1 <= 2)
print(1 >= 2)

#########IF-ELIF-ELSE

if 1 < 2:  # warunek
    print('1 jest mniejsze od 2')  # jeśli prawda

if 2 < 1:  # warunek
    print('1 jest mniejsze od 2')  # jeśli false i nie ma else to nic sie nie wykona

r_variable = 15
if r_variable > 30:
    print("r>30")
else:
    print("r<=30")

t_variable = 5
if t_variable < 3:
    print("t<3")
elif t_variable == 3:
    print("t=3")
else:
    print("t>3")



