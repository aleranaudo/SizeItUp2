import random
'''
# A list of words that
potential_words = ["money"]

word = random.choice(potential_words)

# Use to test your code:
# print(word)

# Converts the word to lowercase
word = word.lower()

# Make it a list of letters for someone to guess
current_word = ["money"] # TIP: the number of letters should match the word.....
'''
# Some useful variables
guesses = []
maxfails = 10
fails = 0

while fails < maxfails:
	guess = input("guess: ")
	guesses.extend(guess)
	if guess=="m":
		print("u got it!")
		print(guesses)
		continue
	# check if the guess is valid: Is it one letter? Have they already guessed it?

	# check if the guess is correct: Is it in the word? If so, reveal the letters!


	fails = fails+1
	print("You have " + str(maxfails - fails) + " tries left!")
