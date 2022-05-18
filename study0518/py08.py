def isPrime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
answer = 0

for i in range(2, 101):
    if isPrime(i):
        answer += 1
print(answer)
