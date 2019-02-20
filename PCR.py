# A PCR program for Dr. Duan's bioinformatics class
# Written by Cameron Reilly and Tristan Hess, copyright 2019

import random
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt

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
        geneSlice1 = geneHalf1[start:start+250]         
        geneSlice2 = reverseGene[start:start+250]

copies = [geneSlice1, geneSlice2]  # adding the sliced gene to the copy list for duplication purposes

# potential variables for statistics (We may not use these in the end)
avgLength = 0
geneCopy = ""

# Perform PCR for 30 iterations
for i in range(0, 30):
    for j in range(0, len(copies)):        # iterates from index 0 to last index of copies[]
        if len(copies[j]) > 199:            # if the length of the copy is 200 or more, it is used for duplicating
            stop = random.randint(-50, 51) + 200          # determine a stopping point for the copy
            geneCopy = copies[j][:stop]
            copies.append(geneCopy)

# Show the total number of copies made

print ("Total copies made:")
print(len(copies))      # prints the total copies made
copyLengths = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# these should be the statistics for the copy lengths
for x in range(0, len(copies)):
    avgLength += len(copies[x])
    if 149 < len(copies[x]) < 160:  # lengths 150 - 159
        copyLengths[0] += 1
    if 159 < len(copies[x]) < 170:  # lengths 160 - 169
        copyLengths[1] += 1
    if 169 < len(copies[x]) < 180:  # lengths 170 - 179
        copyLengths[2] += 1
    if 179 < len(copies[x]) < 190:  # lengths 180 - 189
        copyLengths[3] += 1
    if 189 < len(copies[x]) < 200:  # lengths 190 - 199
        copyLengths[4] += 1
    if 199 < len(copies[x]) < 210:  # lengths 200 - 209
        copyLengths[5] += 1
    if 209 < len(copies[x]) < 220:  # lengths 210 - 219
        copyLengths[6] += 1
    if 219 < len(copies[x]) < 230:  # lengths 220 - 229
        copyLengths[7] += 1
    if 229 < len(copies[x]) < 240:  # lengths 230 - 239
        copyLengths[8] += 1
    if len(copies[x]) > 239:  # lengths 240 - 250
        copyLengths[9] += 1

# Show the average length of all copies
avgLength = avgLength / len(copies)
print("Average length of copies:")
print(avgLength)

# create graph output and console output for both numeric and visual

lengthLabel = ('150-159', '160-169', '170-179', '180-189', '190-199', '200-209',
               '210-219', '220-229', '230-239', '240-250')
print("Number of copies made between lengths:")
for label in lengthLabel:
    print(label, end=', ')
print("")
print(copyLengths)

y_pos = np.arange(len(lengthLabel))

plt.bar(y_pos, copyLengths, align='center', alpha=0.5)
plt.xticks(y_pos, lengthLabel)
plt.ylabel('Number of Copies')
plt.xlabel('Sequence Length')
plt.show()
