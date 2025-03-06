n = int(input())
word_count = {}
for i in range(n):
    word = input()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(len(word_count))
result = ' '.join(str(word_count[word]) for word in word_count)
print(result)
