def print_hello(n, *value):
    for i in range(n):
        for j in range(len(value)):
            print(value[j])

print_hello(3," 정 보"," 통 신","ㅡㅡㅡㅡㅡ")