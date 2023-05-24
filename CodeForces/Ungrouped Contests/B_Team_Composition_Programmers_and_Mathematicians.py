N = int(input())


for _ in range(N):
    
    math, pro = map(int, input().split())
    
    minimum = min(math, pro)
    ans = min(minimum, (math + pro)//4)
    print(ans)
