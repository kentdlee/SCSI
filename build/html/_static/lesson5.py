found = False
count = 0
low = 1
high = 100
print("Pick a number between 1 and 100")
while not found and low <= high: # the low <= high isn't necessary
    guess = (low + high) // 2
    answer = input("Is your number " + str(guess) + "? ")
    
    if answer.lower() == "yes":
        found = True
    else:
        answer = input("Is it higher or lower? ")
        if answer.lower() == "higher":
            low = guess + 1
        else:
            high = guess - 1
            
    count += 1
            

print("I guessed correctly in",count,"tries.")

    