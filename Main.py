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
        return self.character


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
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']

vowels = ['a', 'e', 'i', 'o', 'u']

consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v',
              'w', 'x', 'z', 'y']


def function():
    length = random.randrange(4, 8)

    word = ''
    for i in range(0, length):
        value = random.random()
        print(str(value))
        if i == 0:
            letter = str(letterList[random.randrange(0, 25)])
        else:
            nextletter(letter)
            index = 0
            while index < len(letterList):
                if letterList[index] < value:
                    letter = letters[index]
                index += 1

        word += letter
    print(word + '\n')


def func():
    for letter in letterList:
        print(letter + " Vowel: " + str(isvowel(letter)) + " Consonant: " + str(isconsonant(letter)))


"0.038 for each letter will equally divide 1 over each letter"
def nextletter(letter):
    if letter == 'a':
        setprobabilities(0.0, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04,
                         0.04, 0.04, 0.04, 0.04, 0.04, 0.04)
    if letter == 'b':
        setprobabilities(0.0, 0.0, .1, .2, .1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                         0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    if letter == 'c':
        setprobabilities(0.0, .1, 0.0, .2, .1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                         0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    if letter == 'd':
        setprobabilities(0.0, .1, .1, 0.0, .1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                         0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    if letter == 'e':
        setprobabilities(0.0, .1, .1, .2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                         0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    if letter == 'f':
        setprobabilities(0.0, .1, .1, .2, .1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                         0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    if letter == 'g':
        setprobabilities(0.0, .1, .1, .2, .1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                         0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    if letter == 'h':
        setprobabilities(0.0, .1, .1, .2, .1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                         0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    if letter == 'i':
        setprobabilities(0.0, .1, .1, .2, .1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                         0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    if letter == 'j':
        setprobabilities(0.0, .1, .1, .2, .1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                         0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    if letter == 'k':
        setprobabilities(0.0, .1, .1, .2, .1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                         0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    if letter == 'l':
        setprobabilities(0.0, .1, .1, .2, .1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                         0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    if letter == 'm':
        setprobabilities(0.0, .1, .1, .2, .1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                         0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    if letter == 'n':
        setprobabilities(0.0, .1, .1, .2, .1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                         0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    if letter == 'o':
        setprobabilities(0.0, .1, .1, .2, .1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                         0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    if letter == 'p':
        setprobabilities(0.0, .1, .1, .2, .1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                         0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    if letter == 'q':
        setprobabilities(0.0, .1, .1, .2, .1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                         0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    if letter == 'r':
        setprobabilities(0.0, .1, .1, .2, .1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                         0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    if letter == 's':
        setprobabilities(0.0, .1, .1, .2, .1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                         0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    if letter == 't':
        setprobabilities(0.0, .1, .1, .2, .1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                         0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    if letter == 'u':
        setprobabilities(0.0, .1, .1, .2, .1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                         0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    if letter == 'v':
        setprobabilities(0.0, .1, .1, .2, .1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                         0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    if letter == 'w':
        setprobabilities(0.0, .1, .1, .2, .1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                         0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    if letter == 'x':
        setprobabilities(0.0, .1, .1, .2, .1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                         0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    if letter == 'y':
        setprobabilities(0.0, .1, .1, .2, .1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                         0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    if letter == 'z':
        setprobabilities(0.0, .1, .1, .2, .1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                         0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

def setprobabilities(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26):
    letterList[0] = p1
    letterList[1] = p2
    letterList[2] = p3
    letterList[3] = p4
    letterList[4] = p5
    letterList[5] = p6
    letterList[6] = p7
    letterList[7] = p8
    letterList[8] = p9
    letterList[9] = p10
    letterList[10] = p11
    letterList[11] = p12
    letterList[12] = p13
    letterList[13] = p14
    letterList[14] = p15
    letterList[15] = p16
    letterList[16] = p17
    letterList[17] = p18
    letterList[18] = p19
    letterList[19] = p20
    letterList[20] = p21
    letterList[21] = p22
    letterList[22] = p23
    letterList[23] = p24
    letterList[24] = p25
    letterList[25] = p26


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
        passnum -= 1
    return array



function()
