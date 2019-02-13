# A PCR program for Dr. Duan's bioinformatics class
# Written by Cameron Reilly and Tristen Hess, copyright 2019

import random
import string
import re

bPairs = "actg"
gene = ""
for i in range(2000):
    gene +=random.choice(bPairs)

print(gene)
regEx = "atg.{197}"
m = re.search(regEx, gene)
amplify = m.group(0)
print (len(amplify))
print (amplify)

