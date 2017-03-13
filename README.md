I noticed there’s a lot repositories dealing with a Monte Carlo estimation for the number pi, but none (at least none that I could find) dealing with the number e (= 2.71828…). This was surprising to me, since in mathematics, the number e is every bit as important as pi. So, to make up a little for this apparent discrimination for e, I thought I’d create a repository just for fun. And in the spirit of the famous “Buffoons Needle Problem”, I’ll state the procedure for simulating e as a sort of physical algorithm (i.e. one that can be implemented via ordinary physical objects like needles and paper). However, a software version of the procedure is easy to see, and I’ll then demonstrate that by translating it into a Python program. Here is the algorithm:

1)  Prepare a piece of paper large enough to write down a square matrix with each side having a length of 2^(n+1). The number n in this case is chosen to be any (but not so small) positive integer that we wish (preferably, choose n > 7). For example, if you choose n = 8, then the dimensions of the matrix will automatically be 512 X 512. If you choose n = 9, the dimensions will be 1024 X 1024, and so on. The higher value you choose for n, the better your estimation of e will be (at least, probabilistically). Note though that 2^(n+1) is an exponential function and thus you don’t want to choose n too large (unless you have a piece of paper larger than the size of the observable universe and have an expected lifespan of an eternity).

2) Fill in the entries of the matrix by following this simple rule: Flip a coin (a fair coin) and if it lands heads, write a 1 in the upper, left-most entry of the matrix. Else (when it lands tails), write down a 0. Continue flipping the coin and filling in the matrix, going row by row, and from left to right in an orderly fashion until the matrix is completely filled with 1’s and 0’s.

3) Next, define a “cluster-miss” to be a row (or column) in the matrix that does not contain a “cluster”, where a “cluster” is defined to be a continuous sequence of the same binary digit appearing exactly n or more times. The n in this case is automatically defined to be the same n already chosen/defined in step 1. For example, if n = 8 was chosen in step 1, then the following is defined as a cluster (1-cluster in this case): “…X X X 1 1 1 1 1 1 1 1 X X X…”. The “X’s” here are called “don’t cares” (i.e. they could be either a 1 or 0). Any sequence of the same binary digit appearing less than n times will not be considered a cluster. Hence, different sized matrices have different sized definitions for a cluster.

4) Now with the term “cluster-miss” defined, begin to search the matrix for these cluster-misses. Start the search by specifically looking for 1-cluster-misses in the rows, and keep track of how many you find. After searching all of the rows, begin searching for 1-cluster-misses in all of the columns. Once done with that (and hence finding all 1-cluster-misses), repeat the search process again by looking 0-cluster-misses. At any given time in the search, the estimation for e is given by the simple ratio: trials/cluster-misses. “Trials” in this case just denotes the how many times that you’ve looked for a cluster-miss (for either digit). Notice that the total # of trials possible for any given matrix is thus 2^(n+3). Hence the final estimation for e will always be 2^(n+3)/total#ofClusterMisses. That concludes the algorithm, but just for clarification, here is an example matrix: 

1 0 0 0 0 0 1 0    

1 1 1 1 1 1 1 0    

1 0 0 0 0 1 0 1   
 
1 0 1 1 0 0 0 1    
 
1 1 1 0 0 1 1 1
 
1 1 0 0 0 1 0 0
 
0 1 1 1 1 1 1 0
 
1 0 0 0 1 0 0 1

A small n = 2 value was chosen here for simplicity. Notice that since n = 2, the cluster size is also automatically defined to be of size 2. Also notice that the matrix length was given by = 2^(n+1)  = 2^(2+1) = 8. And finally, here is all the relevant estimation data contained within:

Total # of 1-cluster-misses in rows = 3.
Total # of 1-cluster-misses in in columns = 1.
Total # of 0-cluster-misses in rows = 2.
Total # of 0-cluster-misses in in columns = 3.
Total # of cluster-misses = 3 + 1 + 2 + 3 = 9.
Total # of trials = 2^(n+3) =2^(2+3) = 32.
Final estimation of e = 32/9 = 3.555…

In this case the outcome was obviously not a good estimation for e, and is an example of why choosing larger integer values for n is important. (The limit of the ratio trials/cluster-misses approaches e as n approaches infinity.)

Good outcomes are also dependent upon the coin being a “fair” coin (i.e. producing true heads/tails randomness). And notice since a good estimation for e is dependent upon true randomness, we can use a tweaked version of this algorithm as a parameter/test for measuring the degree of randomness in a certain set of data. For instance, we can potentially use it (in conjunction with other tests) to measure the over-all effectiveness of a random-number-generator. More specifically, we can take a set of unknown data that we wish to test and use it as the input entries described in step 2 of the algorithm (instead of the coin tossing). If we discover that the procedure produces a ratio far removed from the number e, we can conclude (to a certain high degree of probability) that the given set of data was not random, and that it probably contains encoded/predictable patterns within. (It is worthy to point out though, that the logical converse of this is not necessarily true. In other words, just because a given set of data produces a ratio close to the number e, it does not necessarily mean that the data was random.)

Aside from that possible practical use though, I just think that this kind of experiment is cool because it shows how in even a truly random (i.e. unknowable, i.e. unpredictable) set of data, very knowable (i.e. predictable, i.e. nonrandom) patterns will still emerge.

