low=0
high=100
guessed = 0
inp = ''
while inp != 'c':
	guessed = (low+high)//2
	print('Is your secret number:  '+str(guessed))
	inp=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
	if inp == 'l':
		low = guessed
	elif inp == 'h':
		high = guessed
print('Game over. Your secret number was: '+str(guessed))