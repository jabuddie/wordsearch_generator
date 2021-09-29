#!/usr/bin/env python3

import random
import string

#setup
def print_puzzle():
	for x in range(puzzle_size):
		print('  '.join( puzzle[x] ))
	print('\n')

def print_list():	
	for i, word in enumerate(words_list):
		space = 20-len(word)
		print(word + ' '*space, end=' ') 
		if i % 4 == 3:
			print('\n')

puzzle_size = 0
while not puzzle_size in range(15,26):
	try:
		puzzle_size = int(input('Enter an integer for puzzle size from 15 to 25: '))
	except:
		print('Please try again')

if puzzle_size == 15:
	word_count = 8
if puzzle_size > 15 and puzzle_size <= 20:
	word_count = 12
if puzzle_size > 20 and puzzle_size <= 25:
	word_count = 16


#choose your adventure
random_type = 'Y'
while True:
	puzzle_type_input = input('Enter Y to generate a puzzle using random words and N to supply a list: ')
	puzzle_type = puzzle_type_input.upper()
	if not puzzle_type.isalpha():
		print("Please respond with Y or N")
		continue
	if len(puzzle_type) > 1 or len(puzzle_type) < 1:
		print("Please respond with Y or N")
		continue
	else:		
		if puzzle_type == random_type:
			handle = open('/etc/dictionaries-common/words')
			words_list = handle.readlines()
			handle.close()
			words_list = [ random.choice(words_list).upper().replace("'",'').strip() \
			  for _ in range (word_count) ]
		else:			
			words_list = []		
			for input_word_count in range(1, (word_count+1)):
				print("Enter word number ", input_word_count, ': ' )
				input_word = input()
				if not input_word.isalpha() or len(input_word) > 20:
					print("Error please try again. Only respond with only alphanumeric words with a length less than 20")
					exit()
				else:
					words_list.append(input_word.upper().replace("'",'').strip())
		break

#build puzzle
puzzle = [ [ '_' for _ in range (puzzle_size) ] for _ in range (puzzle_size) ]


orientations = [ 'leftright', 'updown', 'diagonalup', 'diagonaldown' ]

for word in words_list:
	word_length = len(word)

	placed = False
	while not placed:

		orientation = random.choice(orientations)

		if orientation == 'leftright':
			step_x = 1
			step_y = 0
		if orientation == 'updown':
			step_x = 0
			step_y = 1
		if orientation == 'diagonalup':
			step_x = 1
			step_y = 1
		if orientation == 'diagonaldown':
			step_x = 1
			step_y = -1

		x_starting = random.randrange(puzzle_size)
		y_starting = random.randrange(puzzle_size)

		ending_x = x_starting + word_length*step_x
		ending_y = y_starting + word_length*step_y

		if ending_x < 0 or ending_x >= puzzle_size: continue
		if ending_y < 0 or ending_y >= puzzle_size: continue


		failed = False

		for i in range(word_length):
			character = word[i]

			new_position_x = x_starting + i*step_x
			new_position_y = y_starting + i*step_y

			character_at_new_position = puzzle[new_position_x][new_position_y]
			if character_at_new_position != '_':
				if character_at_new_position == character:
					continue
				else:
					failed = True
					break

		if failed:
			continue
		else:
			for j in range(word_length):
				character = word[j]

				new_position_x = x_starting + j*step_x
				new_position_y = y_starting + j*step_y

				puzzle[new_position_x][new_position_y] = character

			placed = True
#print answer key            
print_puzzle()
            
for x in range(puzzle_size):
    for y in range(puzzle_size):
        if ( puzzle[x][y] == '_' ):
            puzzle[x][y] = random.choice(string.ascii_uppercase) 
            
#print completed puzzle
print_puzzle()
print_list()

















