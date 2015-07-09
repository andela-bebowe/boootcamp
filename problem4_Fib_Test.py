'''
Testing input from user
Test to ensure argument passed to function is an integer of reasonable size less than 1000.
Test to ensure series gotten from function is correct.
Test to ensure number of elements in series is correct.
'''
import unittest, problem4_fib
class FibTest(unittest.TestCase):
	def test_arg(self):
		self.assertEqual(problem4_fib.fib_main("hgg"), -1, msg = "Strings are not allowed so should return false")
		self.assertEqual(problem4_fib.fib_main(5.88), -1, msg = "Floats not allowed")
		self.assertEqual(problem4_fib.fib_main('&'), -1, msg = "Characters not allowed")
		self.assertEqual(problem4_fib.fib_main(0), -1, msg = "You really dont want to see the series")
		self.assertEqual(problem4_fib.fib_main(-3), -1, msg = "Negative number not allowed")
		self.assertEqual(problem4_fib.fib_main(12000), -1, msg = "Too large a number")
	def test_fib_gen(self):
		self.assertEqual(problem4_fib.fib_gen(5), [0, 1, 1, 2, 3], msg = "Checking results for 5")
		self.assertEqual(problem4_fib.fib_gen(9), [0, 1, 1, 2, 3, 5, 8, 13, 21], msg = "Checking results for 9")
	def test_fib_length(self):
		self.assertEqual(len(problem4_fib.fib_gen(5)), 5, msg = "Checking length of sequence for 5")
		self.assertEqual(len(problem4_fib.fib_gen(13)), 13, "Checking length of sequence")
		self.assertEqual(len(problem4_fib.fib_gen(6)), 6, msg = "Checking length of sequence for 6")
		self.assertEqual(len(problem4_fib.fib_odd(5)), 5, msg = "Checking length of sequence for 6")
		self.assertEqual(len(problem4_fib.fib_even(6)), 6, msg = "Checking length of sequence for 6")
		self.assertEqual(len(problem4_fib.fib_odd(7)), 7, msg = "Checking length of sequence for 6")
		self.assertEqual(len(problem4_fib.fib_even(8)), 8, msg = "Checking length of sequence for 6")
	def test_fib_sum(self):
		self.assertEqual(problem4_fib.fib_sum(5), 7, msg = "Is sum correct")
		self.assertEqual(problem4_fib.fib_sum(9), 54, msg = "Sum working incorrectly")
		self.assertEqual(problem4_fib.fib_sum(4, "odd"), 5, msg = "Odd working incorrectly")
		self.assertEqual(problem4_fib.fib_sum(2, "even"), 2, msg = "even working incorrectly")
if __name__ == '__main__':
	unittest.main()	
