#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)
# 1. Prompt the user: Ask the user to enter a sentence.
# 2. Split the sentence
# 3. Create lists to store words and their corresponding frequencies.
# 4. Iterate through words and update frequencies

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

user_input = input("Enter a sentence: ")

while (is_sentence(user_sentence) == False):
    print("This does not meet the criteria for a sentence.")
user_sentence = input("Enter a sentence: ")

# ---- Prompt + validate sentence ----
sentence = input("Enter a sentence: ").strip()
while not (len(sentence) > 0 and sentence[0].isupper() and sentence[-1] in ".?!" and any(c.isalpha() for c in sentence)):
    print("Please enter a valid sentence (start with a capital and end with . ? or !).")
    sentence = input("Enter a sentence: ").strip()

# ---- Normalize and split ----
text = sentence.lower()
for ch in ".?!,;:":
    text = text.replace(ch, " ")
tokens = text.split()

# ---- Count using two parallel lists (no dictionaries) ----
words = []
counts = []

for w in tokens:
    if w in words:
        i = words.index(w)
        counts[i] = counts[i] + 1
    else:
        words.append(w)
        counts.append(1)

# ---- Print results (encounter order) ----
i = 0
while i < len(words):
    print(words[i] + ": " + str(counts[i]))
    i = i + 1


