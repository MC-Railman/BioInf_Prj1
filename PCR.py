# A PCR program for Dr. Duan's bioinformatics class
# Written by Cameron Reilly and Tristan Hess, copyright 2019

import random

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

geneSlice1 = ""     # will hold a segment of length 250 from the start position we determine
geneSlice2 = ""     # max length we can copy is 200+-50, so 250 is the max length we can potentially copy

# loop to get good primers
badPrimers = True
while badPrimers:
    # randomly pick 200 to be copied
    start = random.randint(1, 1701)

    # check the first 20 over all 2000 for unique primers ON BOTH STRANDS
    primer1 = ""
    primer2 = ""
    for i in range(20):
        primer1 += geneHalf1[i+start]
        primer2 += reverseGene[i+start]

    if geneHalf1.count(primer1) == 1 and reverseGene.count(primer2) == 1:
        badPrimers = False
        geneSlice1 = geneHalf1[start:start+250]         # segment we will copy from 5' to 3'
        geneSlice2 = geneHalf2[start:start+250]         # segment we will copy from 3' to 5'

copies = [geneSlice1, geneSlice2]  # adding the sliced gene to the copy list for duplication purposes

# potential variables for statistics (We may not use these in the end)
brokenCopies = 0
avgLength = 0
geneCopy = ""

# TODO Dr. Duan: "everything from here down is in a for loop"
# TODO Verify that copies under length 200 are still created, but not used for duplication
for i in range(0, 30):      # 30 iterations of PCR duplicating
    for j in range(0, len(copies)):        # iterates from index 0 to last index of copies[]
        if len(copies[j]) > 199:            # if the length of the copy is 200 or more, it is used for duplicating
            stop = random.randint(-50, 51) + 200          # determine a stopping point for the copy
            geneCopy = copies[j][:stop]
            copies.append(geneCopy)


# This is how I checked if the copies worked properly, because all I know how to do is print. All were length 200 to 250

#for x i# n range(0, len(copies)):
    #print(copies[x])
#print(len(copies))

# TODO: Pandas to create graph


