print("enter the  two digit number of your choice");
x=int(input())

print("This is the following menu options\n");
print("----------1.Choose here for incrementing the number-----------------\n");
print("----------2.Choose here for decrementing the number-------------------\n");
print("----------3.EXIT THE PROGRAM----------------------------\n");
print("enter the choice");
y=int(input())
def incr(x):
      x=x+1
      return x
def decr(y):
      y=y-2
      return y
if(y==1):
      x=incr(x)
      print(x)
elif(y==2):
      x=decr(x)
      print(x)
else:
      sys.exit()
      
