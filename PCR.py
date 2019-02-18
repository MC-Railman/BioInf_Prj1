# A PCR program for Dr. Duan's bioinformatics class
# Written by Cameron Reilly and Tristen Hess, copyright 2019

import random
import string
import re

bPairs = "actg"
geneHalf1 = ""
geneHalf2 = ""

# randomly generate half a DNA sequence
for i in range(2000):
    geneHalf1 +=random.choice(bPairs)

# create the other half of the DNA sequence
for letter in geneHalf1:
    if letter == 'a':
        geneHalf2 += 't'
    if letter == 't':
        geneHalf2 += 'a'
    if letter == 'c':
        geneHalf2 += 'g'
    if letter == 'g':
        geneHalf2 += 'c'

# Reverse second half so it reads from 3' to 5'
reverseGene = "".join(reversed(geneHalf2))
print (geneHalf1)
print (geneHalf2)

# TODO: randomly pick 200 to be copied

# TODO: check the first 20 over all 2000 for unique ON BOTH STRANDS

# TODO: Randomly pick size 150 - 250 to copy of strand and copy

# TODO: use copied strands to make more copies IF they are at least length 200

# TODO: After 30 iterations use pandas to create graph


# print(gene)
# regEx = "atg.{197}"
# m = re.search(regEx, gene)
# amplify = m.group(0)
# print (len(amplify))
# print (amplify)

