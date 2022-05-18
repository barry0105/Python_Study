a = []
for i in range(1,11):
    if i % 2 == 0:
        a.append(i+5)
b = [x+5 for x in range(1,11) if x % 2 ==0]
print(a)
print(b)