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
    length = random.randrange(2, 10)
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


def func():
    for letter in letters:
        print(letter + " Vowel: " + str(isvowel(letter)) + " Consonant: " + str(isconsonant(letter)))


function()
