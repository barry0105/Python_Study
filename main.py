import random
secret = random.randint(1, 99)
guess = 0
tries = 0
print("숫자를 맞춰봐라")
print("숫자는 1~99이고 기회는 6번이다")
while guess != secret and tries < 6:
    guess = int(input("숫자를 입력해라"))
    if guess < secret:
        print("낮다.")
    elif guess > secret:
        print("높다.")

    tries = tries + 1

if guess == secret:
    print("맞췄군")
else:
    print("틀렸군")
    print("사실 숫자는 {}였다네..".format(secret))