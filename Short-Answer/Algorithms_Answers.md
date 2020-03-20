#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)
 With the loop, there is only one operation that needs to be completed. The time will increase as n increases.


b) O(nlog(n))
There are two nested loops witht the outer loop running O(n) anad the inner loop increments exponentially.

c) O(n)
The recursive function will be called as many times as n is passed in for bunnies, linear complexity. 


## Exercise II

Using binary search, split the n-story building in half to get a upper half, lower half, and middle floor to the find floor f to find heights where the dropped eggs won't break. 

Check to see if egg breaks when dropped from the middle floor. If it does break, we drop the upper half, move to the lower half and set a new middle point within the lower half. Repeat the process to see if the egg breaks. 

If the egg does not break, move into the upper half, drop the lower half, and set a a new middle point in the upper half. Repeat the process to see if the egg breaks. 

I think this is a decent solution if the there are a lot of floors. If the building only ad very few floors, iterative search is probably better. 

binary search runtime: O(log(n))


