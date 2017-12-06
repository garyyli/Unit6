#Gary Li
#12/6/17
#zzwords.py

dictionary = open('engmix.txt')

wordCount = 0
for word in dictionary:
    if 'zz' in word:
        print(word.strip())
    wordCount += 1

