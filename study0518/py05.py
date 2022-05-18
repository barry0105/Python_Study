our_pots = {'김규진':10,'김도원':1,'김찬웅':2,'김채은':3,'김태현':5}
for i in our_pots:
    print(i)
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
for i in our_pots:
    print("{}의 집에는 {}개의 냄비가 있다.".format(i, our_pots[i]))
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
for i in our_pots:
    if our_pots[i] >= 3:
        print(i)
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
for i in our_pots:
    if our_pots[i] >= 3:
        print(i)
        break