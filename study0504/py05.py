x = int(input())
age = {10<=x<20:"10대", 30<=x<40:"30대"}.get(True,'10대, 30대가 아님')
print(age)