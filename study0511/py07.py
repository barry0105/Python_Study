array1=[]
for i in range(1, 10, 2):
    array1.append(i*i)
array2 = [i*i for i in range(1, 10, 2)]
array3 = [i*i for i in range(1, 10, 2) if i*i > 30]
array_default = [0 for i in range(10)]
print(array1)
print(array2)
print(array3)
print(array_default)    