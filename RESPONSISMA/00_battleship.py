import os
import random
# def setting_up_board(n):
# 	return ["X" * n for _ in range(n) ]

#string imutable
setting_up_board = lambda n : [ list("X" * n) for _ in range(n) ]

setting_up_ship_location = lambda rows : [random.randint(0, rows-1), random.randint(0, rows-1)] 

def printing_board(board):
	os.system("cls")
	for row in board:
		print(" ".join(row))

def check_user_input():
	user_input = list(map(int, input("Enter the coordinate to launch our missle <x> <y>").split()))

	if user_input == my_ship:
		print("Congrats ! You win the game.")
		return True
	
	my_board[user_input[0]][user_input[1]] = "O"

	return False

win = False
rows = 5
my_board = setting_up_board(rows)
my_ship = setting_up_ship_location(rows)


while not win:
	printing_board(my_board)
	# print(my_ship)
	win = check_user_input()

'''
lists = [ [0, 1, 2], [3, 4, 5]]
for list in lists:
	for item in list:
		print(item, end=" ")
	print()

# texts = []
# text = "X" * 3
# for i in range(3):
# 	texts.append(text)

texts = ["X" * 3 for _ in range(3)]

#print(texts)
#texts = ["XXX", "XXX", "XXX"]
'''
# for text in texts:
# 	for char in text:
# 		print(char, end=" ")
# 	print()

'''
for text in texts:
	print(" ".join(text))
'''