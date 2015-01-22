__author__ = 'Baal'
import random


class Letter:
    character = ''
    probability = 0.0

    def __init__(self, character, probability):
        self.character = character
        self.probability = probability

    def isconsonant(self):
        if self.character == 'b' or self.character == 'c' or self.character == 'd' or self.character == 'f' or \
                        self.character == 'g' or self.character == 'h' or self.character == 'j' or self.character == 'k' \
                or self.character == 'l' or self.character == 'm' or self.character == 'n' or self.character == 'p' \
                or self.character == 'q' or self.character == 'r' or self.character == 's' or self.character == 't' \
                or self.character == 'v' or self.character == 'w' or self.character == 'x' or self.character == 'z':
            return True
        return False


    def isvowel(self):
        if self.character == 'a' or self.character == 'e' or self.character == 'i' or self.character == 'o' or \
                        self.character == 'u' or self.character == 'y':
            return True
        return False


    def __repr__(self):
        return self.probability


    def __str__(self):
        return self.character + ": " + str(self.probability)


    def __gt__(self, other):
        """

        :type other: Letter
        """
        return self.probability > other.probability


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


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z']

probabilities = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

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
l = Letter('l', 0.3)
m = Letter('m', 0.0)
n = Letter('n', 0.1)
o = Letter('o', 0.4)
p = Letter('p', 0.0)
q = Letter('q', 0.0)
r = Letter('r', 0.2)
s = Letter('s', 0.0)
t = Letter('t', 0.0)
u = Letter('u', 0.0)
v = Letter('v', 0.0)
w = Letter('w', 0.5)
x = Letter('x', 0.0)
y = Letter('y', 0.0)
z = Letter('z', 0.0)

letterList = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]

vowels = ['a', 'e', 'i', 'o', 'u']

consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v',
              'w', 'x', 'z', 'y']


def function():
    length = random.randrange(4, 8)
    print(letterList[1])
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

    for letter in shortbubblesort(letterList):
        print(letter.character + ": " + str(letter.probability))
    return None


def func():
    for letter in letters:
        print(letter + " Vowel: " + str(isvowel(letter)) + " Consonant: " + str(isconsonant(letter)))


def shortbubblesort(alist):
    array = alist
    exchanges = True
    passnum = len(array) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if array[i] < array[i + 1]:
                exchanges = True
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
        passnum = passnum - 1
    return array


def nextletter(letter):
    if letter == 'a':
        letterList[0] = 0;
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

def aprobabilities():
    letterList[0] = 0
    letterList[1] = 0
    letterList[2] = 0
    letterList[3] = 0
    letterList[4] = 0
    letterList[5] = 0
    letterList[6] = 0
    letterList[7] = 0
    letterList[9] = 0
    letterList[10] = 0
    letterList[11] = 0
    letterList[12] = 0
    letterList[13] = 0
    letterList[14] = 0
    letterList[15] = 0
    letterList[16] = 0
    letterList[17] = 0
    letterList[18] = 0
    letterList[19] = 0
    letterList[20] = 0
    letterList[21] = 0
    letterList[22] = 0
    letterList[23] = 0
    letterList[24] = 0
    letterList[25] = 0




function()
