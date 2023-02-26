numWords = int(input())
words = []

for _ in range(numWords):
    words.append(input())

for word in words:
    print(word[:2] + '... ' + word +'?' )