#Gary Li
#12/13/17
#quiz6.py

dictionary = open('engmix.txt')

#program3
'''number = int(input('Enter a number: '))
for words in dictionary:
    if len(words) == number+1:
        print(words)
        break'''

#program2
'''i = 0
for words in dictionary:
    if words.strip() != '':
        if words.strip()[0]== 'r':
            i=i+1
print(i)'''

#program5
'''L = []
for words in dictionary:
    L.append(words.split())
middle = len(L)
if middle%2 == 0:
    print(L[middle/2-1])
else:
    print(L[middle//2])'''
    
#program1
'''list = []
for words in dictionary:
    if words.count('c') == 3 and words.count('p') == 2:
        list.append(words)
for wordList in list:
    wordList.strip()
    print(wordList)'''


        
