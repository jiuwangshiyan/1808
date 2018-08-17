import random
for i in range(3):
	player = int(input('1.石头 2.剪刀 3.布'))
	commputer = random.randint(1,3)
	if ((player == 1 and commputer == 2)or (player == 2 and commputer == 3)or(player == 3 and commputer == 1)):
		print('玩家赢')
	elif player == commputer:
		print('平局')
	else:
		print('电脑赢')
