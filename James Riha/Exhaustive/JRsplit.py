#this is an attempt to program an algorithm by James and Riha 
#to generate graphs given a degree sequence

#########begin initialization################

y=()
v=[]
m=0
size=0
B=[]
x=[]

#initialize the array x

#this function takes in all the required parameters from the invoking function
def funIn(m1,size1,B1):
    global m 
    global size
    global B
    global x
    global y
    global v
    m=m1
    size=size1
    B=B1
    y=()
    v=[]
    x = [0 for i in range(0, size)]
    return jrr()
#######end initialization#################


#the argument rep is the right end-point of a putative solution
#returns the left end-point of a solution
#note rep is a local variable. The arguments of any function are, for that matter. 
def genSoln(rep):
    i = rep #necessary ? 
    global m  #this declaration makes sure that m refers to a global variable
    while (m > B[i]):
        x[i] = B[i]
        m = m - B[i]
        i = i -1 
    x[i] = m
    m = m - x[i]
    riri(x)
    return i

#find the sum of the B-array entries from 0 to k
def tailSum(k):
    sum = 0
    for j in range(0, k+1):
        sum = sum + B[j]
    return sum

#This is a crucial piece of the solution
#we redefine m and k from two places in the program:
#when k = 0 and when m is too large to allow a redistribution in a tail segment 
def regen(k):
    i = k #necessary ?
    global m
        #global x #doing this is fine; x is a global array for this function
    m = m + x[i]
    x[i] = 0
    while (x[i] == 0 and i < size - 1):
        i = i + 1
    return i

def riri(u):
    #this is the function that adds to the tuple while making sure that the immutability is maintained 
    global y
    global v
    y=y+tuple(u)
    v=u
    
#initial solution; here we can check if m is too large 
def jrr():
    global m
    global size
    b=[]
    del b[:]
    if (m > tailSum(size-1)):
        return 
        #Nothing is returned since we make sure that this check is done before invoking this function
    else:
        k= genSoln(size-1)
        flag = 1
        while (flag):
            #do this if we have reached the left end of the array 
            #while generating a solution
            if (k == 0):
                k= regen(k)
                if (x[k] == 0):
                    break #this results in breaking out of the outer while-loop
                    #flag = 0
            #as long as m is too large for redistribution 
            while (m >= tailSum(k-1)):
                k = regen(k)
                #check if we have reached the right end of the array without
                #finding a non-zero element
                if (x[k] == 0):
                    flag = 0
                    break  #this breaks out of the while loop only ? Yes. 
                           #That's why lines 124-127 was being executed in an
                           #infinite loop. That's why the outer loop
                           #has to be controlled by a flag
            #redefine m amd k to generate a new solution
            if (flag == 1):
                m = m + 1
                x[k] = x[k] - 1
                k = k - 1
                k= genSoln(k)
    if size!=1:
        b=list(zip(*[iter(list(y))] * len(v)))
    else:
        b.append(tuple(y))
    return b

