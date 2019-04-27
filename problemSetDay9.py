# File name: problemSetDay9.py
import random
list1 = ["mother", "father", "sister"]
word_length = len(list1)
random_index = random.randint(0,word_length-1)
print(list1[random_index])
word = list1[random_index]
word_listversion = list(word)