# 3.Write a program to reverse the array.

## Function definition
def reverse(arr):
    i=0
    j=len(arr)-1
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    return arr

## Driver code
arr=[1,2,3,4,5,6]
print("Original Array", arr)
result=reverse(arr)
print("Array after reversing", arr)