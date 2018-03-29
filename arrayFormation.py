# Let the array A contains 5 integers : 7 , 21 , 18 , 3 , 12 then the content of queue and stack will be :
# Queue : 7 , 3
# Stack : 12 , 18 , 21

# Input Format:
# First line contains an integer n as input denoting total numbers of integers in the array.
# Next line contains n space separated integers denoting the elements of array A.
# Your output should print two arrays , one in each line. First line should be the contents of queue and second line should be the contents of stack.

# Output Format:
# In the first line print the contents of queue and in second line print the contents of the stack.

# SAMPLE INPUT:
# 5
# 7 21 18 3 12

# SAMPLE OUTPUT:
# 7 3 
# 12 18 21 

def queue_and_stack (A):
    A=list(A)
    maxlength=max(A)
    prime=SieveOfEratosthenes(maxlength+1)
    queue=[]
    stack=[]
    out=[]
    for i in A:
        if(prime[i]==True):
            queue.append(str(i))
        else:
            stack.append(i)
    print(' '.join(queue))
    print(' '.join(map(str,stack[::-1])))
    return []
    
def SieveOfEratosthenes(n):
     
    # Create a boolean array "prime[0..n]" and initialize
    #  all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
         
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
             
            # Update all multiples of p
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1
    return prime
 
 
 
 
n = int(input())
A = map(int, input().split())
 
out_ = queue_and_stack(A)
for i_out_ in out_:
    print (' '.join(map(str, i_out_)))