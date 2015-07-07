
def search_file(file_txt):
	retain = ""
	my_file = open(file_txt, "r")
	
	line_number = 1
	count = 0
	total_count = 0
	cha = ""
	while line_number < 2015:
		no_upper = 0
		no_lower = 0
		no = 0
		retain = my_file.readline()
		retain_list = list(retain)
		for check in retain:
			if check.isupper():
				no_upper += 1
			elif check.islower():
				no_lower += 1
			else:
				no += 1
		#the conditional below can be changed depending on what u want
		if no_upper >= 4 and no_lower >= 2 and no == 5:
			count += 1
			print retain
		line_number += 1
	return count
print search_file("password.txt")