#Step 1
import random

word_list = ["aardvark", "baboon", "cammel"]

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
n = 0
for letter in word_to_guess:
	n += 1
	if letter == guess:
		word_on_display_list[n-1] = letter
word_on_display = ''.join(word_on_display_list)

print(word_on_display)


# _____________THIS IS WHERE I AM LEFT________________________________________

# Check if the user has won: #75
