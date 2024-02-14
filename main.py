# you can improve user experience by clearing the screen on each stage of the game
# # you can do it by importing <from replit import clear> and then using <clear()> function
# # but I used PyCharm to write the code, and it doesn't work in pycharm
import random
from game_art import logo, stages
from game_words import word_list

word_to_guess = random.choice(word_list)
# Printing the word to ease the code writing:
print(f"(<<< CODE Help: Pssst, the solution is '{word_to_guess}'.>>>)")

# Define a variable to keep track of the player's lives:
lives = 6

# Ask user to choose a letter:
# Add it in a loop, so it asks for input until all the letters are guessed
# Display the stages so user can see lives left
# Display the word to be guessed with the characters hidden:
word_on_display_list = []
for letter in word_to_guess:
	word_on_display_list += "_"
word_on_display = ''.join(word_on_display_list)

end_of_game = False
while not end_of_game:
	if lives > 0:
		print(logo)
		print(stages[lives])
		print(word_on_display)
		guess = input("Please enter a letter: ").lower()

	# check if the chosen letter is in the word to be guessed:
	# if the letter is in the word then replace the respective hidden character in displayed word.
	# if letter is not in the word then lives goes down by 1
		n = 0
		if guess in word_on_display:
			print(f"you already guessed '{guess}'")
		if guess in word_to_guess:
			print("Well done.")
			for letter in word_to_guess:
				n += 1
				if letter == guess:
					word_on_display_list[n-1] = letter
			word_on_display = ''.join(word_on_display_list)

			if "_" not in word_on_display:
				end_of_game = True
				print("You won!")
		else:
			lives -= 1
			print(f"Sorry! '{guess}' is not in the word.")
	else:
		print("You lost ...")
		end_of_game = True
