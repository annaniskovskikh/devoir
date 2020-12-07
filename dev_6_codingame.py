# -*- coding: utf-8 -*-

print("-------The 2nd exercise-------\n")

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def verify_next_nb(tel_numbers):
    dico_nbs = {}
    nb_numbers = 0
    for nb in tel_numbers:
        if nb[0] not in dico_nbs.keys():
            dico_nbs[nb[0]] = []
            nb_numbers += 1
        elif nb[0] in dico_nbs.keys():
            dico_nbs[nb[0]].append(nb[1:])

    for key, value in dico_nbs.items():
        print(value, file=sys.stderr, flush=True)
        if dico_nbs[key] != []:
            nb_numbers += verify_next_nb(value)

    return nb_numbers

n = int(input())
nbs = []
for i in range(n):
    telephone = input()
    nbs.append(telephone)
    nbs.sort()
    
cn_numbers = verify_next_nb(nbs)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

# The number of elements (referencing a number) stored in the structure.
print(cn_numbers)