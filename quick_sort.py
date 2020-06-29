def quicksort(arr):
	if len(arr) < 2:
		return arr
	else:
		pivot = arr[0]
		less = [i for i in arr[1:] if i <= pivot]
		greater = [i for i in arr[1:] if i > pivot]
		return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([7,6,5,4,3,2,2,2,1]))