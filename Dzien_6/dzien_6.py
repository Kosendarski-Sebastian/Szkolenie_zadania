# 1.	LESSER OF TWO EVENS: Napisz funkcję, która zwraca mniejszą
# z dwóch podanych liczb jeśli obie liczby są parzyste,
# ale zwraca większą, jeśli jedna lub obie liczby są nieparzyste
# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5
#


def lesser(a, b):
    if a < b:
        return a
    else:
        return b


def greater(a, b):
    if a > b:
        return a
    else:
        return b


def check_parity(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return True
    else:
        return False


def lesser_of_two_evens(a, b):
    if check_parity(a, b):
        print(lesser(a, b))
        return lesser(a, b)
    else:
        print(greater(a, b))
        return greater(a, b)


lesser_of_two_evens(12, 13)


# ----------------------------------------------------------------------------------------------
#
# 2.	ANIMAL CRACKERS: Napisz funkcję pobiera ciąg składający się z dwóch słów i zwraca True,
# jeśli oba słowa zaczynają się od tej samej litery
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False


def animal_crackers(user_input):
    word = user_input.split(" ")
    if word[0][0].upper == word[1][0].upper:
        print(word[0][0], word[1][0])
        return True
    else:
        print(word[0][0], word[1][0])
        return False


print(animal_crackers("Kot Kot"))


# -------------------------------------------------------------------
# 3.	MAKES TWENTY: Biorąc pod uwagę dwie liczby całkowite,
# zwróć True, jeśli suma liczb całkowitych wynosi 20
# lub, jeśli jedna z liczb całkowitych wynosi 20. Jeśli nie, zwróć False
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False

def makes_twenty(a, b):
    if a + b == 20 or a == 20 or b == 20:
        print("TRUE")
        return True
    else:
        print("FALSE")
        return False


makes_twenty(3, 1)
makes_twenty(5, 15)
makes_twenty(-10, 30)
makes_twenty(-10, 20)
makes_twenty(26, 20)


# ---------------------------------
# 4.	OLD MACDONALD:
# Napisz funkcję, w której pierwszą i czwartą literę nazwy zaczyna się od pierwszej i czwartej litery
# old_macdonald('macdonald') --> MacDonald
# Przykladowo: 'macdonald'.capitalize() returns 'Macdonald'

def cap14(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return "too short"


print(cap14("macdonald"))


# ------------------------------------------------------

# 5.	MASTER YODA: zwróć zdanie z odwróconymi słowami
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'
# Uwaga: W tym przypadku przydatna może być metoda .join().
# Metoda .join() umożliwia łączenie ze sobą ciągów w listę z jakimś ciągiem łącznika.
# Na przykład niektóre zastosowania metody .join():
# >>> "--".join(['a','b','c'])
# >>> 'a--b--c'
# Oznacza to, że jeśli masz listę słów, które chcesz zamienić z powrotem w zdanie,
# możesz po prostu połączyć je pojedynczym ciągiem spacji:
# >>> " ".join(['Hello','world'])
# >>> "Hello world"


def master_yoda(str):
    vector = str.split()
    vector.reverse()
    print(vector)
    return " ".join(vector)


print(master_yoda('I am home'))


# ------------------------------------
# 6.	ALMOST THERE: Biorąc pod uwagę liczbę całkowitą n, zwróć True, jeśli n jest w zakresie 10 od 100 lub 200
# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True
# abs(num) zwraca wartosc absolutna


def almost_there(num):
    if abs(100 - num) <= 10 or abs(200 - num) <= 10:
        return True
    else:
        return False


print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(89))


# -------------------------------------------------
# 7.	FIND 33:
# Mając listę wartości int, zwróć True, jeśli tablica zawiera 3 obok 3 gdzieś.
# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False


def has_33(lst):
    counter = 0
    for i in range(len(lst) - 1):
        if lst[i + 1] == 3 and lst[i] == 3:
            counter += 1
        else:
            counter += 0
    if counter > 0:
        return True
    else:
        return False


print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))


# ---------------------------
# 8.	PAPER DOLL: Biorąc pod uwagę ciąg, zwróć ciąg, w którym na każdy znak w oryginale znajdują się trzy znaki
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'


def paper_doll(text):
    return "".join(e * 3 for e in text)


print(paper_doll("Aktuariusz"))


# ----------------------------------------------------------------------
# 9.	BLACKJACK: Biorąc pod uwagę trzy liczby całkowite od 1 do 11,
# jeśli ich suma jest mniejsza lub równa 21, zwróć ich sumę.
# Jeśli ich suma przekracza 21 a jest jedenaście, zmniejsz sumę o 10.
# Na koniec, jeśli suma (nawet po dostosowaniu) przekracza 21, zwróć 'BUST'
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19


def blackjack(i, j, k):
    if i + j + k <= 21:
        return i + j + k
    elif i + j + k > 21 and (i == 11 or j == 11 or k == 11):
        result = i + j + k - 10
        if result <= 21:
            return result
        else:
            return "BUST"
    else:
        return "BUST"


print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(11, 11, 11))
