#Write a program to find all pairs of an integer array whose sum is equal to a given number?

def getPairsCount(arr, n, sum):

	count = 0
	
	for i in range(0, n):
		for j in range(i + 1, n):
			if arr[i] + arr[j] == sum:
				count += 1

	return count


arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6
print("Given array: ",arr,
'\n'"To find pairs with sum: ",sum)
print("Count of pairs with above sum: ",
	getPairsCount(arr, n, sum))

