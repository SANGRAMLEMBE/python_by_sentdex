game = [[0, 0, 0],
	    [0, 0, 0],
	    [0, 0, 0],]


#print("   a  b  c")
'''count = 0

# tic tac toe
for row in game:
	print(count, row)
	count = count+1
'''
'''
#function [6]
def game_board():
	print("   a  b  c")
	for count,row in enumerate(game):
		print(count,row)

game_board() 
game[0][1] = 1

game_board()

'''






'''
game[0][1] = 1

# build in function [5]
for count,row in enumerate(game):
	print(count,row)

'''

'''
def game_board(player=0,row=0,column=0,just_display=False):
	print("  0  1  2")
	if not just_display:
		game[row][column] = player

	for count, row in enumerate(game):
		print(count,row)

game_board(just_display = True)
game_board(player = 1, row=1,column=2)
'''

'''
def game_board(player=0,row=0,column=0,just_display=False):
	print("  0  1  2")
	if not just_display:
		game[row][column] = player

	for count, row in enumerate(game):
		print(count,row)

print(game)
game_board(player = 1, row=1,column=1)
print(game)

'''

def game_board(game_map,player=0,row=0,column=0,just_display=False):
	try:
		print("  0  1  2")
		if not just_display:
			game_map[row][column] = player
		for count, row in enumerate(game_map):
			print(count, row)
		return game_map
	except IndexError as e:
		print("Error:make sure your input row / column  0 1 2 ?",e)


game = game_board(game,just_display=True)
game = game_board(game,player=1,row=3 , column=2)