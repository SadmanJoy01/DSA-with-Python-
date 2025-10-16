# Sum of element

# Initialize an array (list) of integers
arr = [1, 2, 3, 4, 5]

# Initialize a variable to store the total sum, starting at 0
total = 0

# Loop through each element 'j' in the array 'arr'
for j in arr:
    # Add the current element 'j' to the total
    total = total + j

# After the loop ends, print the total sum of all elements
print(total)
# End

# Min Max finder

# Create a list (array) of numbers
arr = [1, 2, 3, 4, 5]

# Initialize the minimum value with the first element of the list
minvalue = arr[0]

# Initialize the maximum value with the first element of the list
maxvalue = arr[0]

# Loop through each element 'j' in the list 'arr'
for j in arr:
    # If the current element is smaller than the current minimum, update minvalue
    if j < minvalue: 
        minvalue = j 
    
    # If the current element is larger than the current maximum, update maxvalue
    if j > maxvalue:
        maxvalue = j 
        
# After the loop ends, print the smallest number found
print("Min value", minvalue)

# Print the largest number found
print("Max value", maxvalue)
#End
