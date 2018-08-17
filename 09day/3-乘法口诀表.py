i = 1

while i < 10:
	c = 1
	while c <= i:
		print('%d*%d=%d'%(c,i,c*i),end='\t')
		c+=1
	print('')
	i+=1
