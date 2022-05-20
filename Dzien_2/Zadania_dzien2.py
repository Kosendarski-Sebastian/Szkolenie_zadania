# Zad1

no_of_employees = 1

if no_of_employees > 0 and no_of_employees < 10:
    print("mała")
elif no_of_employees >= 10 and no_of_employees < 50:
    print("średnia")
elif no_of_employees >= 50 and no_of_employees < 100:
    print("duża")
elif no_of_employees > 100:
    print("bardzo duża")
else: print("błędna ilość pracowników")

# Zad2

name = "Andrzej"
if name[-1] == "a":
    print("imię " + str(name) + " jest żeńskie")
else:
    print("imię " + str(name) +  " jest męskie")

#Zad3

username = input()
if username.capitalize() == "Bond": #capitalize uniewrażliwia na wielkość liter z inputa
    print("Welcome on board 007")
else:
    print("Welcome on board Sebastian")

