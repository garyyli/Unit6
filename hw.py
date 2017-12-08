dictionary = open('engmix.txt')
tf = False
word = input('Enter a word: ')
for words in dictionary:
    if wods == words:
        tf = True
        
if tf == True:
    print(word, 'is in the dictionary')
else:
    print(word, 'is not in the dictionary')