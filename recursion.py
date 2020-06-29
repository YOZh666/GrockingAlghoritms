def countdown(i):
	print(i)
	if i<=0:
		return
	else:
		countdown(i-1)

def factorial(x):
	if x == 1:
		return 1
	else:
		return x * factorial(x-1)

print("COUNTDOWN WITH RECURSION:")
countdown(5)
print("FACTORIAL:")
print(factorial(10))


def recurs_sum(arr):
	if arr == []:
		return 0
	return arr[0] + recurs_sum(arr[1:])

def count(arr):
	if arr == []:
		return 0
	return 1 + count(arr[1:])


def recursion_max(arr):
	if len(arr) == 2:
		return arr[0] if arr[0] > arr[1] else arr[1]
	sub_max = recursion_max(arr[1:])
	return arr[0] if arr[0] > sub_max else sub_max


print("Recursion Summ:")
print(recurs_sum([2,4,6]))
print("Recursion len:")
print(count([1,2,3,4,5]))
print("recursion_max")
print(recursion_max([55,756,2145,8674,232]))

