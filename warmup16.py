#Gary Li
#12/11/17
#warmup16.py

dictionary = open('engmix.txt')

for words in dictionary:
    if words.strip() != '':
        if words.strip()[0]= 'g':
            if words.strip()[-1]= 'l':
                print(words)
