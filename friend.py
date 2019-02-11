###for when the times get tough, and the path looks rough###
from datetime import datetime;
from script import hanoi_game;

###function to decide how day was and how to handle that
def gotta_keep_your_head_up(user_answer):
	answer = user_answer.lower()
	if answer == 'good' or answer == 'yes':
		print('Awesome! I\'m so glad to hear that.\n')
		highlights = input('\nIs there anything particular you\'d like to tell me about today?\n')
		print('That is Epic!\n')
		new_answer = input('Anything else happen that was good?\n')
		gotta_keep_your_head_up(new_answer)
	elif answer == 'bad':
		print('I\'m sorry to hear that. Keep your head up!\n')
		lowlights = input('\nWhat happened today to get you down? Tell me all about it.\n')
		new_answer = input('Anything else happen that was bad, maybe good?\n')
		gotta_keep_your_head_up(new_answer)
	elif answer == 'lonely' or answer == 'alone':
		print('I\'m sorry you feel alone. I\'m here for you as a friend and listening ear.\n')
		low_lights = input('Any way I can help\n')
		new_answer = input('Did anything good or bad happen today?\n')
		gotta_keep_your_head_up(new_answer)
	elif answer.find('bored'):
		print('Well, there\'s always time to be bored, but what if we play a game?\n')
		game = input('Would you like to play Hanoi game? or fibonacci?')
		if game.lower() == 'hanoi':
			hanoi_game()
			new_input = input('Anything else you would like to share with me?')
			gotta_keep_your_head_up(new_input)
	elif answer == 'good bye' or answer == 'bye' or answer == 'no':
		return
user_input = input('How was your day? \n')
gotta_keep_your_head_up(user_input)