"""
From chatgpt

Problem: 
    title : sum of multiples 
    
    Write a function that takes two numbers, n and m, and returns
      the sum of all multiples of n that are less than m. For example, 
      if n = 3 and m = 10, the function should return 18 (which is the sum of 3, 6, and 9).    

"""


def sum(n : int ,m : int) -> int : 
  sum = 0 
  for num in range(m):
    if num * n < m and (num * n ) % n == 0 and num  != 0:
      sum += num * n 
  return sum 


print(sum(3, 10))