#Gary Li
#12/6/17
#fileDemo.py - how to read a file

dictionary = open('engmix.txt')

wordCount = 0
for word in dictionary:
    wordCount += 1
    
print('There are', wordCount, 'words in the dicionary.')