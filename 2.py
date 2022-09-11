# Write a program to reverse an array in place?

def reverseList(arr, start, end):
	while start < end:
		arr[start], arr[end] = arr[end], arr[start]
		start += 1
		end -= 1

arr = [1, 2, 3, 4, 5, 6]
print("Original array: ",arr,)
reverseList(arr, 0, 5)
print("Reversed array: ",arr,)

