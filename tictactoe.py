from numpy.random import choice

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
			'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
			'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
	print('-+-+-')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print('-+-+-')
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def check_win_condition(current_player):
	global theBoard
	top_row = theBoard['top-L'] + theBoard['top-M'] + theBoard['top-R']
	mid_row = theBoard['mid-L'] + theBoard['mid-M'] + theBoard['mid-R']
	low_row = theBoard['low-L'] + theBoard['low-M'] + theBoard['low-R']
	l_col = theBoard['top-L'] + theBoard['mid-L'] + theBoard['low-L']
	m_col = theBoard['top-M'] + theBoard['mid-M'] + theBoard['low-M']
	r_col = theBoard['top-R'] + theBoard['mid-R'] + theBoard['low-R']
	diagonal = theBoard['top-L'] + theBoard['mid-M'] + theBoard['low-R']
	antidiagonal = theBoard['low-L'] + theBoard['mid-M'] + theBoard['top-R']
	
	#cycle through players
	if top_row.count(current_player) == 3:
		return current_player
	elif mid_row.count(current_player) == 3:
		return current_player
	elif low_row.count(current_player) == 3:
		return current_player
	elif l_col.count(current_player) == 3:
		return current_player
	elif m_col.count(current_player) == 3:
		return current_player
	elif r_col.count(current_player) == 3:
		return current_player
	elif diagonal.count(current_player) == 3:
		return current_player
	elif antidiagonal.count(current_player) == 3:
		return current_player

	return None



def setSquare(square, value):
	global theBoard
	theBoard[square] = value

#randomly determine who goes first
players = ['X', 'O']
rows = ['top', 'mid', 'low']
cols = ['L', 'M', 'R']

turn = choice(players)

for x in range(9):
	chosen_turn_address = None
	while not chosen_turn_address:
		chosen_row = choice(rows)
		chosen_col = choice(cols)
		temp_address = chosen_row + '-' + chosen_col	
		if theBoard[temp_address] == ' ':
			chosen_turn_address = temp_address
			setSquare(chosen_turn_address, turn)
			print('Turn {}: filling {} with an {}'.format(x+1, chosen_turn_address, turn))
			winner = check_win_condition(turn)
			#print(winner)
			if winner:
				print('***************************')
				printBoard(theBoard)
				print('***************************')
				print('Congratulations, player {} winning on turn {}'.format(winner, x+1))
				exit()
		
		else:
			print(">> spot {} is occupado, rerolling ...".format(temp_address))

	if turn == 'X':
		turn = 'O'
	else:
		turn = 'X'

# Draw
print('****************************')
printBoard(theBoard)
print('****************************')
print('DRAW! Better luck next game!')