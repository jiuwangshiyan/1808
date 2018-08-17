acc = 'yxy'
pwd = 123456
i = 0
while i < 3:
	a = input('请输入帐号')
	b = int(input('请输入密码'))
	if acc == a and pwd == b:
		print('登录成功')
		xz = int(input('选择英雄范围0.ADC 1.肉 3.法师'))
		if xz == 0:
			print('鲁班大师')
		elif xz == 1:
			print('程咬紧')
		elif xz == 3:
			print('王邵军')
		break
	else:
		print('输入有误')	
	
