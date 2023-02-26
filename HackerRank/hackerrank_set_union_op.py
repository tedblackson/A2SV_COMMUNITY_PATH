# Enter your code here. Read input from STDIN. Print output to STDOUT
engNum = int(input())
engStudents = set(map(int, input().split()))
frenchNum = int(input())
frenchStudents = set(map(int, input().split()))

totalSet = engStudents.union( frenchStudents)
print(len(totalSet))