square_dict = dict()  #pusty słownik

for number in range(1,11):
    square_dict[number] = number*number

print(square_dict)

square_dict2 = {number : number*number for number  in range(1,11)}
print(square_dict2)


wizzards = ["Harry", "Hermiona", "Ron"]
data = {}

for element in wizzards:
    data[element] = len(element)

data2 = {i : len(i) for i in wizzards}

print(data)
print(data2)

wizzards_grades= {
    "Harry" : [1,1,2,3],
    "Hermione" : [5,5,5,5],
    "Ron" : [2,3,1,1]
}

final_grades = {wizzard : sum(grades)/len(grades) for wizzard, grades in wizzards_grades.items()}
print(final_grades)


nerds = {wizzard :sum(grades) / len(grades) for wizzard, grades in wizzards_grades.items() if sum(grades) / len(grades) > 4.7}
print(nerds)


final_grades2= {
    "Harry" : 3.25,
    "Hermione" : 5.0,
    "Ron" : 3.0,
    "Neville": 4.25,
    "Luna": 4.75,
    "Draco" : 3.5
}
statuses = {wizzard: "nerd" if grade > 4.75 else "lazy" for wizzard, grade in final_grades2.items() }
print(statuses)



numbers_3 = [i**i for i in range(1,11) if i%2==0]
print(numbers_3)


sekwencja = "ACCGTA"
zasady = ["puryna" if z == "A" or z == "G" else "piramidyna" for z in sekwencja]
print(zasady)

sekwencja_male_litery = [z.lower() for z in sekwencja]
print(sekwencja_male_litery)


values =  [ 12,32,34,45,56,78]
letters = ["a","b","c","d","e","f"]

data3 = [(o, w) for o, w in zip(letters,values)]
print(data3)

data4 = list(zip(letters,values))
print(data4)

dlugie = ['AGACAAGAA', 'TTTCAAGG', 'GGAGACCTA', 'AAGGTTAAA']
krotkie = ["AGA", "AGG"]
wynik =[]
for d in dlugie:
    for k in krotkie:
        wynik.append([d,k, k in d])

print(wynik)

for k, d, t in wynik:
    print(f"{k},{d},{t}")

wynik2 = [[d,k,k in d] for d in dlugie for k in krotkie]
print(wynik2)


restaurants = ["MCDonald","KFC","KFC", "Burger King", "Burger king"]
uniqe_restaurants = set(restaurants)
print(uniqe_restaurants)


number = 78789789
name = "Thomas"

print("My name is %s" % name)
print("My number is %d" % number)
print("My number is %d and my name is %s" %(number,name))
print("My number is %(number)d and my name is %(name)s" %{"number": number, "name": name})

pi = 3.14159265
print("%.3f" % pi )

print ("Hello {}".format(name))
print ("Hello {} and my num {}".format(name, number))

print(f"My number is {number} and my name is {name}".format(name = name, number = number))


liczba_kotow = 5
nowy_napis ="{kto} ma {ile} kotow".format(kto = "Ala", ile = liczba_kotow)
print("Have a nice day".split(" "))

out_template = """If a grocery store sells ice bags at $ {} per bag, with a profit margin of {} %,
then the total profit it makes by selling {} ice bags is $ {}."""

cost_ice_bag = 4
profit_margin = 20
number_of_sold_bags = 100
total_profit = cost_ice_bag * (profit_margin/100)*number_of_sold_bags
our_message = out_template.format(cost_ice_bag,profit_margin,number_of_sold_bags,total_profit)
print(our_message)

print("{0} {1} {2}".format("swinki", "trzy", "cztery"))
print("{2} {1} {0}".format("swinki", "trzy", "cztery"))


x =10
y=11
print (f"x = {x}, y= {y}, x+y = {x+y}")