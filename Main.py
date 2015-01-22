__author__ = 'Baal'
import random

class Letter:
    character = ''
    value = 0.0

    def __init__(self, character, value):
        self.character = character
        self.value = value

    def isconsonant(self):
        if character == 'b' or character == 'c' or character == 'd' or character == 'f' or character == 'g' or character == 'h' or character == 'j' or character == 'k' or character == 'l' or \
                        character == 'm' or character == 'n' or character == 'p' or character == 'q' or character == 'r' or \
                        character == 's' or character == 't' or character == 'v' or character == 'w' or character == 'x' or character == 'z':
            return True
        return False

    def isvowel(self):
        if character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u' or character == 'y':
            return True
        return False


def isconsonant(a):
    if a == 'b' or a == 'c' or a == 'd' or a == 'f' or a == 'g' or a == 'h' or a == 'j' or a == 'k' or a == 'l' or \
                    a == 'm' or a == 'n' or a == 'p' or a == 'q' or a == 'r' or \
                    a == 's' or a == 't' or a == 'v' or a == 'w' or a == 'x' or a == 'z':
        return True
    return False


def isvowel(a):
    if a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u' or a == 'y':
        return True
    return False


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']

a = Letter('a', 0.0)
b = Letter('b', 0.0)
c = Letter('c', 0.0)
d = Letter('d', 0.0)
e = Letter('e', 0.0)
f = Letter('f', 0.0)
g = Letter('g', 0.0)
h = Letter('h', 0.0)
i = Letter('i', 0.0)
j = Letter('j', 0.0)
k = Letter('k', 0.0)
l = Letter('l', 0.0)
m = Letter('m', 0.0)
n = Letter('n', 0.0)
o = Letter('o', 0.0)
p = Letter('p', 0.0)
q = Letter('q', 0.0)
r = Letter('r', 0.0)
s = Letter('s', 0.0)
t = Letter('t', 0.0)
u = Letter('u', 0.0)
v = Letter('v', 0.0)
w = Letter('w', 0.0)
x = Letter('x', 0.0)
y = Letter('y', 0.0)
z = Letter('z', 0.0)

letterList = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]

vowels = ['a', 'e', 'i', 'o', 'u']

consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v',
              'w', 'x', 'z', 'y']

letterProbabilities2 = dict([('a', 1), ('b', 2), ('c', 3), ('d', 0), ('e', 0), ('f', 0), ('g', 0), ('h', 0), ('i', 0),
                            ('j', 0), ('k', 0), ('l', 4), ('m', 0), ('n', 0), ('o', 0), ('p', 0), ('q', 0), ('r', 0),
                            ('s', 0), ('t', 0), ('u', 5), ('v', 0), ('w', 0), ('x', 0), ('y', 0), ('z', 0)])

letterProbabilities = {'a': 1, 'b': 2, 'c': 3, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0,
                       'j': 0, 'k': 0, 'l': 4, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0,
                       's': 0, 't': 0, 'u': 5, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}


def function():
    length = random.randrange(4, 8)
    "print(length)"
    word = ''
    for i in range(0, length):
        value = random.random()
        if i == 0:
            letter = letters[random.randrange(0, 25)]
        elif isconsonant(letter):
            letter = vowels[random.randrange(0, len(vowels))]
        elif isvowel(letter):
            letter = consonants[random.randrange(0, len(consonants))]
        word += letter
    print(word + '\n')
    sort2(letterProbabilities, letters, 5)
    for key, value in sort2(letterProbabilities.items(), letters, 5):
        print(key + ": " + str(value))
    return None


def func():
    for letter in letters:
        print(letter + " Vowel: " + str(isvowel(letter)) + " Consonant: " + str(isconsonant(letter)))


def sort(dictionary):
    arr = dictionary
    i = 0
    j = i + 1
    while i < len(sorted):
        i += 1
        while j < len(sorted):
            j += 1
            if sorted[i] > sorted[j] and i != j:
                temp = sorted[j]
                sorted[j] = sorted[i]
                sorted[i] = temp
    return sorted


def sort2(dictionary, array, randomValue):
    arr = array

    i = 0
    print(dictionary['a'])
    j = i + 1
    while i < len(arr):
        i += 1
        while j < len(arr):
            j += 1
            print(str(dictionary[arr[i]]))
            "if the letter probability value is less than the previous letter probability value," \
                " move it toward the end of the fucking dictionary"
            if dictionary[arr[i]] < dictionary[arr[j]] and i != j:
                temp = dictionary[arr[j]]
                dictionary[arr[j]] = dictionary[arr[i]]
                dictionary[arr[i]] = temp
    return dictionary


def nextletter(letter):
    if letter == 'a':
        "t"
    if letter == 'b':
        "t"
    if letter == 'c':
        "t"
    if letter == 'd':
        "t"
    if letter == 'e':
        "t"
    if letter == 'f':
        "t"
    if letter == 'g':
        "t"
    if letter == 'h':
        "t"
    if letter == 'i':
        "t"
    if letter == 'j':
        "t"
    if letter == 'k':
        "t"
    if letter == 'l':
        "t"
    if letter == 'm':
        "t"
    if letter == 'n':
        "t"
    if letter == 'o':
        "t"
    if letter == 'p':
        "t"
    if letter == 'q':
        "t"
    if letter == 'r':
        "t"
    if letter == 's':
        "t"
    if letter == 't':
        "t"
    if letter == 'u':
        "t"
    if letter == 'v':
        "t"
    if letter == 'w':
        "t"
    if letter == 'x':
        "t"
    if letter == 'y':
        "t"
    if letter == 'z':
        "t"


function()
