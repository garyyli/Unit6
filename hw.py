"""dictionary = open('engmix.txt')
tf = False
word = input('Enter a word: ')
for words in dictionary:
    if word == words.strip():
        tf = True
        
if tf == True:
    print(word, 'is in the dictionary')
else:
    print(word, 'is not in the dictionary')"""

dictionary = open('engmix.txt')
L = []
for words in dictionary:
    L.append(words.split())
    
num = int(input('Enter a number: '))
print(L[num-1])