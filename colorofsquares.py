gridPos = input("Enter a chess board position: ")

col = gridPos[0].lower()
row = int(gridPos[1])

if col in "aceg":
	colStartswithBlack = True
else:
	colStartswithBlack = False
	
	
if colStartswithBlack:
	if row % 2 == 0:
		white = True
	else:
		white = False
else:
	if row % 2 == 0:
		white = False
	else:
		white = True
		
if white:
	print("That position square is White.")
else:
	print("That position square is Black.")
