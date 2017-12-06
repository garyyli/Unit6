#Gary Li
#12/6/17
#howManyWords.py

dictionary = open('engmix.txt')
if len(words)=1:
    
wordCount = 0
for word in dictionary:
    if 'gary' in word:
        print(word.strip())
    wordCount += 1
    
print('There are', wordCount, 'words in the dicionary.')
