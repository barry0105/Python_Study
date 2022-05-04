score = int(input())
result = {score >= 90:"A", 80<= score < 90:"B", 70<= score < 80:"C", 60<= score < 70:"D", score<60:"D"}.get(True)
print(result)