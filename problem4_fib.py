numb = 10
def fib_main(num):
	if type(num) != int or num <= 0 or num >= 12000:
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

def fib_sum(num):
	fib_main(num)
	seq_list = fib_gen(num)
	seq_list_sum = 0
	for numb in seq_list:
		seq_list_sum += numb
	return seq_list_sum

print fib_gen(numb)
print fib_sum(numb)

