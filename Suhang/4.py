our_pots={'일지매':1,'이무기':2,'삼지창':3,'사오정':4,'오징어':5}
for i in our_pots.keys():
    if our_pots[i] >= 3:
        print(i)
        break