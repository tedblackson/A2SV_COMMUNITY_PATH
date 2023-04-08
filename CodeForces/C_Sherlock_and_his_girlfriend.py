n = int(input())

is_prime = [True for _ in range(2, n + 2)]


d= 2

while d * d <= (n + 2):
    