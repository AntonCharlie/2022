"""
--------------------------------------
|       song		|	  counter	 |		
--------------------------------------
|Tegar				|	    100	 	 |
|Terima Kasih Cinta	| 		60		 |
|Mungkinkan			| 		50		 |
|Manusia Bodoh		| 		30		 |
|Seandainya			|		25		 |
--------------------------------------
"""
def find_smallest(list):
	smallest_val = list[0]
	smallest_index = 0

	for i in range(1, len(list)):
		if list[i] < smallest_val:
			smallest_val = list[i]
			smallest_index = i

	return smallest_index

def find_greatest(list):
	greatest_val = list[0]
	greatest_index = 0

	for i in range(1, len(list)):
		if list[i] > greatest_val:
			greatest_val = list[i]
			greatest_index = i

	return greatest_index


def selection_sort(list):
	a = input()
	new_list = []
	if a == "desc":
		for i in range(len(list)):
			greatest_index = find_greatest(list)
			new_list.append(list.pop(greatest))
	elif a == "asc":
		for i in range(len(list)):
			smallest_index = find_smallest(list)
			new_list.append(list.pop(smallest))

	return new_list

daftar_angka = [10, 4, 10, 3, 1, 0, 8, 9]

print(selection_sort(daftar_angka))
