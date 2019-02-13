# A PCR program for Dr. Duan's bioinformatics class
# Written by Cameron Reilly and Tristen Hess, copyright 2019

import random
import string

bPairs = "actg"
gene = ""
for i in range(2000):
    gene +=random.choice(bPairs)

print(gene)