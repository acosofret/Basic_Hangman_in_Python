#Step 1
import random

word_list = ["aardvark", "baboon", "camel"]

word_to_guess = random.choice(word_list)
# Printing the word to ease the code writing:
print(f"(<<< CODE Help: Pssst, the solution is '{word_to_guess}'.>>>)")

# Display the word to be guessed with the characters hidden:
word_on_display_list = []
for letter in word_to_guess:
	word_on_display_list += "_"
word_on_display = ''.join(word_on_display_list)

print(word_on_display)

# Ask user to choose a letter:
guess = input("Please enter a letter:\n").lower()

# check if the chosen letter is in the word to be guessed:
# if the letter is in the word then replace the respective hidden character in displayed word.


# _____________THIS IS WHERE I AM LEFT________________________________________


#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].


#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
