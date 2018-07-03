import itertools

file = open("wordsEn.txt","r")
words = frozenset([x.strip() for x in file.readlines()])
jumble = input("What is the jumbled word? ")
jumblePerms = frozenset(["".join(x) for x in itertools.permutations(jumble)])
print("The possible solutions are:")
solutions = words.intersection(jumblePerms)
for word in solutions:
    print("  "+word)
                 
