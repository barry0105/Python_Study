table = [[[1, 2],[3,4]],[[5, 6],[7,8]]]
for i in table:
    for j in i:
        for k in j:
            print(k)
        print(j)
    print(i)