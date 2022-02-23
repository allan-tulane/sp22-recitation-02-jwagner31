
"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
import math
###

def simple_work_calc(n, a, b):
  """Compute the value of the recurrence $W(n) = aW(n/b) + n
  
  Params:
  n......input integer
  a......branching factor of recursion tree
  b......input split factor
  
  Returns: the value of W(n).
  """
  if(n <= 1):
    return 1
  else:
    totalWork = a*simple_work_calc(n//b, a, b)+n
    return totalWork


def test_simple_work():
  """ done. """
  assert simple_work_calc(10, 2, 2) == 36
  assert simple_work_calc(20, 3, 2) == 230
  assert simple_work_calc(30, 4, 2) == 650
  
  assert simple_work_calc(20,2,2) == 92
  assert simple_work_calc(5,4,2) == 29
  assert simple_work_calc(22,2,2) == 96

def work_calc(n, a, b, f):
  """Compute the value of the recurrence $W(n) = aW(n/b) + f(n)
  
  Params:
  n......input integer
  a......branching factor of recursion tree
  b......input split factor
  f......a function that takes an integer and returns 
       the work done at each node 
  
  Returns: the value of W(n).
  """
  if(n <= 1):
    return 1
  else:
    totalWork = a*work_calc(n//b, a, b, f)+f(n)
    return totalWork

def test_work():
  """ done. """
  assert work_calc(10, 2, 2,lambda n: 1) == 15
  assert work_calc(20, 1, 2, lambda n: n*n) == 530
  assert work_calc(30, 3, 2, lambda n: n) == 300
  
  #test cases for question 4
  assert work_calc(40, 2, 2, lambda n: 1) == 63
  #log(n) test case commented out due to log(n) returning decimal values. Value about 
  #equal to 75.
  #assert work_calc(40, 2, 2, lambda n: math.log(n)) == 41
  assert work_calc(40, 2, 2, lambda n: n) == 224

def span_calc(n, a, b, f):
  """Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)
  
  Params:
  n......input integer
  a......branching factor of recursion tree
  b......input split factor
  f......a function that takes an integer and returns 
         the work done at each node 
  
  Returns: the value of W(n).
  """
  if(n <= 1):
    return 1
  else:
    totalSpan = span_calc(n//b, a, b, f)+f(n)
    return totalSpan


def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
	result = []
	for n in sizes:
		# compute W(n) using current a, b, f
		result.append((
			n,
			work_fn1(n),
			work_fn2(n)
			))
	return result

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'W_1', 'W_2'],
							floatfmt=".3f",
							tablefmt="github"))

def test_compare_work():
  # curry work_calc to create multiple work
  # functions taht can be passed to compare_work
  
  # create work_fn1
  # create work_fn2
  work_fn1 = lambda n:work_calc(n,4,2,lambda n:n**1.5) #c<log_b(a)
  work_fn2 = lambda n:work_calc(n,4,2,lambda n:n**3) #c>log_b(a)
  work_fn3 = lambda n:work_calc(n,4,2,lambda n:n**2) #c=log_b(a)
  res = compare_work(work_fn1, work_fn2)
  res2 = compare_work(work_fn2, work_fn3)
  print_results(res)
  print_results(res2)
test_compare_work()

def test_compare_span():
  span_fn1 = lambda n:span_calc(n,2,2,lambda n:1)
  span_fn2 = lambda n:span_calc(n,2,2,lambda n:math.log(n))
  res = compare_span(span_fn1, span_fn2)
  span_fn3 = lambda n:span_calc(n,2, 2, lambda n:n))
  span_fn4 = lambda n:span_calc(n,2, 2, lambda n:n*n))
  res2 = compare_span(span_fn3, span_fn4)
  print_results(res)
  print_results(res2)

test_compare_span()