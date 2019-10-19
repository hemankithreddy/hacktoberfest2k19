def arm(n):
	l=str(n)
	leng=len(l)
	cube=0
	for i in range(leng):
		cube=cube+int(l[i])**leng
	return cube
while True:
	x=int(input("enter a number:"))
	if(x>0):
		y=arm(x)
		break
	else:
		print('Wrong input')
if(x==y):
	print('The entered number is an armstrong number')
else:
	print('The entered number is not an armstrong number')
