
num = 0
a = int(input('请输入一个数字'))
b = int(input('请输入一个数字'))
count = 0
'''
if a > b:
	count = b
	while count <= a:
		num += count
		count += 1
'''
if a < b:
	count = a
	while count <= b:
		num += count
		count += 1
#print(num)


#num = 0
#a = int(input('请输入一个数字'))
#b = int(input('请输入一个数字'))
#count = 0
if a > b:
	count = a
	while count >= b:
		num += count
		count -= 1
		

print(num)



