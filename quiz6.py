#Gary Li
#12/13/17
#quiz6.py

dictionary = open('engmix.txt')

#program2
'''for words in dictionary:
    i = 0
    if words.strip() != '':
        if words.strip()[0]== 'r':
            i=i+1

print(i)'''

#program5
L = []
for words in dictionary:
    L.append(words.split())
middle = len(L)
if middle%2 == 0:
    print(words[middle/2-1], words[middle/2])
else:
    print(words[middle//2])
