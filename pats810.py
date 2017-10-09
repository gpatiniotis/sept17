sm=0
m=-2
n=-1
while  m==n or m<n or m<0 or n<0:
    n=int(raw_input("doste 1 thetiko arithmo"))
    m=int(raw_input("doste enan  megalytero thetiko arithmo"))
for i in range(n,m+1):
    if (i%n==0):
        sm=sm+i
        print i
print "to athroisma ton pollaplasion toy %d (mazi me ayto) mexri to %d (mazi me ayto) einai %d"%(n,m,sm)
