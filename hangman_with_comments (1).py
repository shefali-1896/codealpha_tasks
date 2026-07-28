# Import random module to select a random word
import random

# Create a list of words for the game 
words = ["python", "laptop","computer","codealpha","linkedin"]

# Select one random word from the list 
word = random.choice(words)

# Print the selected word (for testing only)
#print(word)

# create the empty list to store hidden letters
display = []

# Add one underscore (_) for each letter in the selected word
for letter in word:
    display.append("_")

# Total chances for the player 
lives = 6

while lives > 0:

    # Ask the user to enter a letter
    guess = input("Enter a letter:")

    #Check if the guessed letter i present in the word
    if guess in word:
        print("Correct Guess!")

        # Find the position of each letter in the word
        for position in range(len(word)):

            # Check if the guessed letter matches the current letter
            if word[position] == guess:

                # Replace underscrore wiith the guessed letter
                display[position] = guess
    else:
        print("Wrong Guess!")

        # Reduce one life for a wrong guess
        lives = lives - 1
        print("Lives Left:", lives)

    # Clean formatmain word sow  karein 
    print(" ".join(display))

    # Chcek if the player has guessed all letters
    if "_" not in display:
        print("You Win!")
        break

    # Check if lives are over
    if lives == 0:
        print("Game Over!")
        print("The word was:", word)
        break
