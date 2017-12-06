#Gary Li
#12/6/17
#longestDictionaryWord.py

dictionary = open('engmix.txt')

longestWord = 0
i = ''
for word in dictionary:
    if len(word)>=longestWord:
        longestWord = len(word)
        i = word

print(i)

