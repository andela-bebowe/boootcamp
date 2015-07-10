def fib_main(num):
	if type(num) != int or num <= 0 or num >= 60:
		print "illegal variable, not int,less than zero or greater than 60"
		return -1

def fib_gen(num):
	fib_main(num)
	a, b = 1, 0
	c = 0
	seq_list = []
	while num > 0:
		seq_list.append(c)
		b = a
		a = c
		c = a + b
		num -= 1
	return seq_list

def fib_sum(num, b = None):
	seq_list_sum = 0
	if b == None:
		seq_list = fib_gen(num)
		for number in seq_list:
			seq_list_sum += number
		return seq_list_sum
	elif b == "even":
		even_list = fib_even(num)
		for number in even_list:
			seq_list_sum += number
		return seq_list_sum
	elif b == "odd":
		odd_list = fib_odd(num)
		for number in odd_list:
			seq_list_sum += number
		return seq_list_sum

def fib_even(num):
	seq_list = fib_gen(num + 20)
	even_list = []
	for numb in seq_list:
		if numb % 2 == 0:
			even_list.append(numb)
	while len(even_list) > num:
		del(even_list[num])
	return even_list

def fib_odd(num):
	seq_list = fib_gen(num + 20)
	odd_list = []
	for numb in seq_list:
		if numb % 2 != 0:
			odd_list.append(numb)
	while len(odd_list) > num:
		del(odd_list[num])
	return odd_list