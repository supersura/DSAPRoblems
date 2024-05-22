# 4.write a program to reverse the string.
def reverseString(str):
    str=str[::-1] ## Means we are starting :ending, staring from last , if we use +1 then it will print in the non reversal order, -1 indicates to print from backward
    return str

## Driver code
str="Suraj"
result = reverseString(str)
print(result)