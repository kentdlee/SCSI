import itertools

file = open("wordsEn.txt","r")
words = [x.strip() for x in file.readlines()]
jumble = input("What is the jumbled word? ")
lst = ["".join(x) for x in itertools.permutations(jumble)]
print("The possible solutions are:")
for perm in lst:
    # if a student doesn't know about the "in" operator
    # on lists, then they can code it by iterating over the list
    # of words.
    # It might be good to point out how much faster the "in" operator
    # is. This is because "in" is implemented in C since it is built into
    # the Python interpreter. Anything built into the interpreter will run
    # faster but stil with the same big-Oh complexity.
    # if perm in words:
    #    print("  "+perm)    
    for word in words:
        if word == perm:
            print("  "+perm)
                 
