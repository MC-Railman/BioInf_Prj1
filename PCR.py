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

# loop to get good primers
badPrimers = True
while badPrimers:
    # randomly pick 200 to be copied
    start = random.randint(1, 1701)
    end = start + 200

    # check the first 20 over all 2000 for unique primers ON BOTH STRANDS
    primer1 = ""
    primer2 = ""
    for i in range(20):
        primer1 += geneHalf1[i+start]
        primer2 += reverseGene[i+start]


    if geneHalf1.count(primer1) == 1 and reverseGene.count(primer2) == 1:
        badPrimers = False


# TODO: Randomly pick size 150 - 250 to copy of strand and copy
copies = []
for i in range(start, end):
    # this will help with adjusting random size variation somehow but idk yet
    e = random.randint(-50, 51)



# TODO: use copied strands to make more copies IF they are at least length 200

# TODO: After 30 iterations use pandas to create graph
