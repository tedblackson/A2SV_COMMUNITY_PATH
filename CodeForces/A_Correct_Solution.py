number = input()
bobs = int(input())

arr = list(map(int, list(str(number))))

arr.sort()
if number == 0 :
    if bobs == number:
        print("WRONG_ANSWER")
    
    exit()
    

answer = ""
zeroes = 0

    
for ele in arr:
    if ele == 0:
        zeroes += 1
    else:
        answer += str(ele)
answer = answer[0] + zeroes * "0" + answer[1:]
print(answer)

answer = int(answer)
if answer ==  bobs:
    print("OK")
else:
    print("WRONG_ANSWER")