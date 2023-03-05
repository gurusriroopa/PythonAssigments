list1 = [1, 2,3,4,5,6,7,8,9]
even_num = 0
odd_num = 0
for n in list1:
  if n % 2 == 0:
    even_num +=1
  else:
      odd_num +=1
print ("Number of even numbers:" , even_num)
print ("Number of odd numbers:" , odd_num)