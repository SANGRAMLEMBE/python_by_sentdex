game = [[2, 0, 2],
        [1, 2, 0],
        [2, 2, 1]]

if game[0][0] == game[1][1] ==game[2][2]:
	print("Winner")

if game[2][0]==game[1][1]==game[0][2]:
	print("winner")