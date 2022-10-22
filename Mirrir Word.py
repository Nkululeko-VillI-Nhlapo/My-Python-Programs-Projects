#This program lets you write a word in reverse
#spuki = ikups

word = input("Please enter any word: \t")
lentswe = ' '

for i in range(len(word)-1,-1,-1):
    lentswe += word[i]

print('The word you gave is {0}, and the mirrored output is {1}'.format(word,lentswe))
print('\n')
print('\n')

