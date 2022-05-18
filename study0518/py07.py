i = 2
j = 1
while i <= 9:
    print("{} * {} = {}".format(i, j, i*j))
    j += 1
    if j > 9:
        j = 1
        i+=1
        print("ㅡㅡㅡㅡㅡ")