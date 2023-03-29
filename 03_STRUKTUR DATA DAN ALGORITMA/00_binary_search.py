my_numbers = [1, 3, 5, 7, 9]

def binary_search(list, item):
	low = 0
	high = len(list) - 1
	while low <= high :
		mid = (low + high) // 2
		guess = list[mid]
		if guess == item:
			return mid
		elif guess > item:
			high = mid - 1
		elif guess < item :
			low = mid + 1
	return None

print(binary_search (my_numbers, 5))
print(binary_search (my_numbers, 11
	))