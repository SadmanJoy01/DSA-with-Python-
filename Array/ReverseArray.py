# Reverse an array

arr = [1,2,3,4,5]

n = len(arr) # finding the length of the array

for i in range(n // 2): # find the middle with iteration
  arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i] # swap the values
  
print("Reversed array is", arr)
