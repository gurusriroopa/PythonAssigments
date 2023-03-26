def square_num(n):
  return n * n
nums = [9, 25, 12, 15]
result = map(square_num, nums)
print(list(result))