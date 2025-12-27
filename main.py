import os
import random
import time

from PyMultiDictionary import DICT_EDUCALINGO, MultiDictionary
from random_word import RandomWords

fruits = []

lives = 5

os.system("cls" if os.name == "nt" else "clear")


def average(words):
    avgWords = words.copy()
    total = 0
    for k in list(avgWords.keys()):
        total += len(k)
        print("".join("_ " for i in range(len(k))), len(k))
    print(
        f"{round(total/len(avgWords.keys()), 2)} is the average number of letters throughout the words.\n"
    )


def guessing(words, lives):
    random.shuffle(list(words.keys()))
    for k in list(words.keys()):
        if lives == 0:
            print("Game Over! \n")
            break

        print("You are now guessing a new word.\n")
        time.sleep(2)
        print(f"{len(k)} letters, {words[k]}")
        word = input("Input your Word: \n")

        if word == k:
            print("You guessed correct!")
            print(f"You still have {lives} lives left \n")
            del words[k]
            continue

        lives -= 1
        print("Unlucky.\n")
        print(f"The word was {k} \n")
        print(f"You have {lives} lives left")


def look_up_word(k):
    dictionary = MultiDictionary()
    definition = dictionary.meaning("en", k, dictionary=DICT_EDUCALINGO)

    origDef = definition[1].lower()
    newDef = origDef.replace(k, "*" * len(k))
    return newDef


def getRandomWord():
    return RandomWords().get_random_word().strip()


def addWords(lives, fruits):
    print("Loading game...")
    for j in range(10):
        k = getRandomWord()
        definition = look_up_word(k)

        while len(definition) == 0:
            k = getRandomWord()
            definition = look_up_word(k)

        fruits[k] = definition


words = dict(fruits)
addWords(lives, words)
average(words)
numWords = len(words.keys())
guessing(words, lives)
print(f"Your Score is {numWords - len(words.keys())} out of {numWords}")
