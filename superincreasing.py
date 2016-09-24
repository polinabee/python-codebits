'''Have the function Superincreasing(arr) take the array of numbers stored in arr and determine if the array 
  forms a superincreasing sequence where each element in the array is greater than the sum of all previous elements. 
  The array will only consist of positive integers. For example: if arr is [1, 3, 6, 13, 54] then your program 
  should return the string "true" because it forms a superincreasing sequence. If a superincreasing sequence isn't formed, 
  then your program should return the string "false"'''
  
  
def Superincreasing(arr):
    ans = 0
    for i in range(0,len(arr)):
        ans = 0 if arr[i] > sum(arr[:i]) else 1
    if ans > 0:
        return "false"
    else:
        return "true"
print Superincreasing(raw_input())
