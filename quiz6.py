#Gary Li
#12/13/17
#quiz6.py

dictionary = open('engmix.txt')

#program2
for words in dictionary:
    i = 0
    if words.strip() != '':
        if words.strip()[0]== 'r':
            i=i+1

print(i)
