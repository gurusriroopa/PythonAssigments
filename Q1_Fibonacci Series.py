n= int(input("Enter Number"))
a = 1
b=1
count=0
if n<=0:
 print("Please enter a positive integer")
elif n==1 :
  print ("Fibonacci sequence upto", n, ":")
  print(a)
else:
  print("Fibonacci sequence:")
  while count < n:
    print(a)
    nth = a + b
    a = b
    b = nth
    count += 1
    


