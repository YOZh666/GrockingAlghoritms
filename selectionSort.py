def find_Smallest(arr):
	smallest = arr[0]
	smallest_index = 0
	for i in range(1, len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
	return smallest_index


def selectionSort(arr):
	newArr = []
	for i in range(len(arr)):
		smallest = find_Smallest(arr)
		newArr.append(arr.pop(smallest))
	return newArr

print(selectionSort([5,123,6,23,68,33,2]))