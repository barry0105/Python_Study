h = " Happy programming! "
print(len(h)) #h의 길이
print(h.count("p")) #p의 갯수
print(h.upper()) #전부 대문자
print(h.lower()) #전부 소문자
print(h.strip()) #앞 뒤 공백 제거
print(h.replace("Happy", "Funny")) #Happy를 Funny로 치환
print(h.find("ap")) #ap가 어디있는지 탐색
print(h.rfind("a")) #a가 어디있는지 거꾸로 탐샙
print(h.find("Happy")) #happy가 몇번 인덱스부터 있는 확인
print(h.find("fun")) #fun이 몇번 인덱스부터 있는지 거꾸로 확인 없어서 -1
print("a" in h) #h안에 a가 있나요?
print("b" in h) #h안에 b가 있나요?

x = "01::23::ab::^^" 
y = x.split("::") #문자를 ::을 기준으로 자르기
print(y)
print(", ".join(y)) #리스트를 , 로 다시 이어붙이기