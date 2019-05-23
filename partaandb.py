# Final Project 113 Morning
# Meriselle Ruotolo
# Chrystal Mingo

import math
from tkinter import *
import tkinter.messagebox
import turtle

def get_letters_and_probability(n):
    N_DISPLAYABLE_CHAR = 54

    # turn all into a single program

    # opens word.txt
    file = open("Words.txt", "r")

    # string filled with all from textfile
    text_string = file.read()

    # letter_count initialized at zero
    letter_count = [0] * N_DISPLAYABLE_CHAR

    # counting the letters                                                  
    for i in range(len(text_string)):
        if text_string[i] == '\n' or text_string[i] == ' ' or text_string[i] == '\t':
            letter_count[53] += 1
        elif ord(text_string[i]) >= 65 and ord(text_string[i]) <= 90:
            letter_count[int(ord(text_string[i]) - 65)] += 1
        elif ord(text_string[i]) >= 97 and ord(text_string[i]) <= 122:
            letter_count[int(ord(text_string[i]) - 97 + 26)] += 1
        else:
            letter_count[52] +=1

    letter_count_pairs = []

    for i in range(N_DISPLAYABLE_CHAR):
        if i == 52:
            letter_count_pairs.append((letter_count[i], '#'))
        elif i >= 0 and i < 26:
            letter_count_pairs.append((letter_count[i], chr(i + 65)))
        elif i >= 26 and i < 52:
            letter_count_pairs.append((letter_count[i], chr(i + 97 - 26)))
        else:   
            letter_count_pairs.append((letter_count[i], ' '))

    # sorting from greatest to least
    sorted_count = sorted(letter_count_pairs, reverse=True)

    # ensuring only letters that exist in the file are able to be chosen for pie chart\
    filtered_counts = []
    for i in range (0, n):
        if (sorted_count[i]) == 0:                                              # if n is greater than the amount of unique characters, only include unique characters
            continue
        filtered_counts.append(sorted_count[i])
        
    # PROBABILITY CALCULATIONS
    probabilities = [0] * n
    total_characters = int(len(text_string))
    for i in range (0, n):
        if (filtered_counts[i]) == 0:
            continue
        probabilities[i] = (int(filtered_counts[i][0]) / total_characters, filtered_counts[i][1])


    return probabilities

# user input
n = 55
while n > 54 or n < 0:
    n = int(input('Please number of letters to be considered in pie chart [ must be less than 54 and greater than 0]: '))

    
print(get_letters_and_probability(n))






