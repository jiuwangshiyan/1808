account = '123'
password = 123456
money = 999
zh = input('请输入帐号')
mm = int(input('请输入密码'))
if zh == account and mm == password:
	print('请取款')
	y = int(input('请输入取款金额'))
	if y > 999:
		print('余额不足')
	else:
		print('取款成功')

else:	
	print('帐号或密码错误')
