# Check if an element exists
 #Linear search algorithm

arr = [3,5,2,4,1]

target = 4
found = False # set a track of finding False, if found then replace with True

for j in arr:
  if j == target:
    found = True
    break # if found stops the iteration 
  
if found:
  print("Element found")
else:
  print("Not fount")
