import random

word = input("Please enter a word: ")
jumble = ""
for c in random.sample(word,len(word)):
    jumble = jumble + c
    
print("A jumble is", jumble + ".")

# Here is an alternative version that creates a permutation of indices
# into the string instead of the characters of the string itself.

#jumble = ""
#for i in random.sample(range(len(word)),len(word)):
    #jumble = jumble + word[i]
    
#print("A jumble is", jumble + ".")