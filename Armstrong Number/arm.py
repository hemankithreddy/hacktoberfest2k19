def arm(n):
	l=str(n)
	leng=len(l)
	for i in range(leng):
		cube=cube+l[i]**3
	return cube
while True:
	x=int(input("enter a number:"))
	if(x>0):
		y=arm(n)
		break
	else:
		print('Wrong input')
if(x==y):
	print('The entered number is an armstrong number")
else:
	print('The entered number is not an armstrong number")

print("Thank you ACM--PESU ECC")
