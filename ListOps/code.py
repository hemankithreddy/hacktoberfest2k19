nums = [3, 5, 2, 9, 101, 333, 4]
i=0
def remove_odd_element(a):
    while i in range(len(a)+1):
      del a[0::2]
      print(a)
      i=i+1
print("[]")
remove_odd_element(nums)
