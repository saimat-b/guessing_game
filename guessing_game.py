# Guessing game the onjective of which is for the 
# user to guess a secret word in 3 attempts.
# By Saimat Balabekova

secret_word = "jupyter"
guess = ""

# Set starting constants
guess_count = 0
guess_limit = 3
out_of_guesses = False 

# Main Game loop with logic
while guess != secret_word and not(out_of_guesses) :
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        # with each increment the user would have had a single guess, therefore:
        guess_count += 1    
        if guess != secret_word :
            print("Try again")
    else:
        out_of_guesses = True
if out_of_guesses:
    print ("Out of Guesses, YOU LOSE!")
else :
    print("You Win!")

