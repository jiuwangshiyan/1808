import random
 
player = int(input('请出1.石头,2.剪刀,3.布'))

computer = random.randint(1,3)

if ((player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1)):
	print('wanjiaying')
elif player == computer:
	print('pingju')
else:
	print('diannaoying')
