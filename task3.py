n = int(input())
words = set()
for i in range(n):
    word = input()
    word = word.lower()
    words.add(word)
l = int(input())
error_words = set()
for i in range(l):
    string = input()
    string = string.lower()
    use_words = string.split(' ')
    for j in use_words:
        if j not in words:
            error_words.add(j)
for i in error_words:
    print(i)
