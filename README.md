# CMPS 2200  Recitation 02

**Name (Team Member 1):** Joe Wagner  
**Name (Team Member 2):** Luke Albright

In this recitation, we will investigate recurrences. 
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.


## Setup
- Make sure you have a Github account.
- Login to Github.
- Login to repl.it, using "sign in with github"
- Click on the assignment link sent through canvas and accept the assignment.
- Click on your personal github repository for the assignment.
- Click on the "Work in Repl.it" button. This will launch an instance of `repl.it` initialized with the code from your repository.
- You'll work with a partner to complete this recitation. To do so, we'll break you into Zoom rooms. You will be able to code together in the same `repl.it` instance. You can choose whose repl.it instance you will share. This person will click the "Share" button in their repl.it instance and email the lab partner.

## Running and testing your code
- In the command-line window, run `./ipy` to launch an interactive IPython shell. This is an interactive shell to help run and debug your code. Any code you change in `main.py` will be reflected from this shell. So, you can modify a function in `main.py`, then test it here.
  + If it seems things don't refresh, try running `from main import *`
- You can exit the IPython prompt by either typing `exit` or pressing `ctrl-d`
- To run tests, from the command-line shell, you can run
  + `pytest main.py` will run all tests
  + `pytest main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Version Control" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$ W(n) = aW(n/b) + f(n) $$

where $W(1) = 1$.

- [ ] 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$.

- [ ] 2. (2 point) Test that your function is correct by calling from the command-line `pytest main.py::test_simple_work` by completing the test cases and adding 3 additional ones.

- [ ] 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases.

- [ ] 4. (2 point) Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = \log n$ and $f(n) = n$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.

We have tested all three functions (1, n, logn ) and they demonstrated that total work calculated matches the asymptotic behavior expected by Big O. For instance, n=1 is the smallest amount of total work as we expect, and it does not blow up at any values of n relatively speaking.  Second in total work comes log(n), which shows an increase of less than O(n) as expected, and the values calculated at the larger values of n match up as expected. Lastly, the work of O(n) was found to be the greatest as expected, and it increased linearly with different values of n.


- [ ] 5. (4 points) Now that you have a nice way to empirically generate valuess of $W(n)$, we can look at the relationship between $a$, $b$, and $f(n)$. Suppose that $f(n) = n^c$. What is the asypmptotic behavior of $W(n)$ if $c < \log_b a$? What about $c > \log_b a$? And if they are equal? Modify `compare_work` to compare empirical values for different work functions (at several different values of $n$) to justify your answer. 

As you can see in the graphs below, c<log_b(a) and when c=log_b(a), the asymptotic behavior is relatively steady. Neither blow up extremely when n is very large. On the other hand, when c is set to be greater than log_b(a) the total work blows up with large values of n. this aligns with what we expected for the asymptotic behaviors orignially.

|     n |    c<log_b(a) |    c>log_b(a) |
|-------|---------------|---------------|
|    10 |       185.599 |          1692 |
|    20 |       831.839 |         14768 |
|    50 |      4813.480 |        236908 |
|   100 |     20253.920 |       1947632 |
|  1000 |   1674822.842 |    1987993280 |
|  5000 |  62313354.782 |  249711292352 |
| 10000 | 250253419.128 | 1998845169408 |
|     n |.   c=log_b(a) |
|-------|.  ------------|
|    10 |.          328 |
|    20 |.         1712 |
|    50 |.        12936 |
|   100 |         61744 |
|  1000 |       8544512 |
|  5000 |     294904064 |
| 10000 |    1279616256 |

- [ ] 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 

The span for everything matches up as expected. When f(n)=1, the span is very small and is only 14 for large values of n. The same goes for log(n) which has relatively small values for span that dont blow up. The span of n grows nearly linearly, but not exactly which is expected due to machine cost differing. The span of n*n blows up for large values of n, which is expected even with span.

|     n |f(n)=1 |f(n)=log(n) |
|-------|-------|--------|
|    10 |     4 |  5.605 |
|    20 |     5 |  8.601 |
|    50 |     6 | 13.506 |
|   100 |     7 | 18.111 |
|  1000 |    10 | 37.786 |
|  5000 |    13 | 56.944 |
| 10000 |    14 | 66.154 |
|     n |f(n)=n | f(n)=n*n |
|-------|-------|-----------|
|    10 |    18 |       130 |
|    20 |    38 |       530 |
|    50 |    97 |      3315 |
|   100 |   197 |     13315 |
|  1000 |  1994 |   1333214 |
|  5000 |  9995 |  33332873 |
| 10000 | 19995 | 133332873 |
