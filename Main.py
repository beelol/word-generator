__author__ = 'Baal'
import random


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

vowels = ['a', 'e', 'i', 'o', 'u']

consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v',
              'w', 'x', 'z', 'y']


def function():
    length = random.randrange(4, 8)
    "print(length)"
    word = ''
    for i in range(0, length):
        if i == 0:
            letter = letters[random.randrange(0, 25)]
        elif isconsonant(letter):
            letter = vowels[random.randrange(0, len(vowels))]
        elif isvowel(letter):
            letter = consonants[random.randrange(0, len(consonants))]
        word += letter
    print(word + '\n')
    return None


def function():
    length = random.randrange(4, 8)
    "print(length)"
    word = ''
    for i in range(0, length):
        if i == 0:
            letter = letters[random.randrange(0, 25)]
        elif letter == 'a':
            letter = vowels[random.randrange(0, len(vowels))]
        elif isvowel(letter):
            letter = consonants[random.randrange(0, len(consonants))]
        word += letter
    print(word + '\n')
    return None


def func():
    for letter in letters:
        print(letter + " Vowel: " + str(isvowel(letter)) + " Consonant: " + str(isconsonant(letter)))


def sort(dictionary):
    sorted = dictionary
    i = 0
    j = i + 1
    while i < len(sorted):
        i = i + 1
        while j < len(sorted):
            j = j + 1
            if sorted[i] > sorted[j] and i != j:
                temp = sorted[j]
                sorted[j] = sorted[i]
                sorted[i] = temp
    return sorted

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
