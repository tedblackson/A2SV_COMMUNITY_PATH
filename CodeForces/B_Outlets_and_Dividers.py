N = int(input())

for _ in range(N):
    students, numDevider = map(int, input().split())
    deviders = list(map(int, input().split()))
    deviders.sort(reverse = True)
    
    curSum = 2
    if students <= 2:
        print(0)
    else:
        for i , ele in enumerate(deviders):
            curSum += ele - 1
            if curSum >= students:
                print(i + 1)
                break
        else:
            print(-1)
        