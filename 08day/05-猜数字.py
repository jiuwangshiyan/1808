import random
num = random.randint(1,100)
i = 1
while i <= 10:
	x = int(input('请猜数'))
	if x < num:
		print('猜小了')
	elif x > num:
		print('猜大了')
	else:
		print('猜中了')
		break
	i += 1	
