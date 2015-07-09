def search_file(file_txt):
	retain = ""
	my_file = open(file_txt, "r")
	line_number = 1
	count = 0
	total_count = 0
	while line_number < len(my_file):
		no_upper = 0
		no_lower = 0
		no = 0
		retain = my_file.readline()
		for check in retain:
			#checks number of uppercase letters
			if check.isupper():
				no_upper += 1
			#checks number of lowercase letters
			elif check.islower():
				no_lower += 1
			#checks number of numbers
			elif check.isdigit():
				no += 1
		#the conditional below can be changed depending on what u want to display
		if no_upper >= 4 and no_lower >= 2 and no >= 4:
			count += 1
		line_number += 1
	#return the number of counts after the while loop	
	return count
print search_file("password.txt")

