from enum import Enum
import random

from PyDictionary import PyDictionary
from py_random_words import RandomWords


dictionary = PyDictionary()
random_input =str(RandomWords().get_word())


print(f"Hint - {dictionary.meaning(random_input)}")
random_word_length = len(random_input)
display = []


for pos in range(random_word_length):
    display += "-"


end_of_game = False
number_of_loops = random_word_length

while not end_of_game and number_of_loops:
    user_word = input("Enter a word \n")
    for position in range(random_word_length):
        if random_input[position] == user_word:
            display[position] = user_word
            number_of_loops+=1

    print(display)
    number_of_loops -= 1
    if "-" not in display:
        end_of_game = True
        print(f"Word is {random_input}")
    elif number_of_loops == 0:
        print(f"""No more inputs allowed, you lost!
The word was {random_input}
        """)



