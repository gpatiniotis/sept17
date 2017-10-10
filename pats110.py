a=[]
mylist=[1]
y="true"
p=0
r=0
while y=="true":
    p+=1
    y="false"
    mylist = raw_input('Eisagetai tin lista me ta probata gia mia nixta(plikrologiste 0 gia na mas dosete ton arxiko arithmo probaton): ')
    mylist = [int(x) for x in mylist.split(',')]
    t=sum(mylist)
    if p==1 :
       
        r=sum(mylist)
 
    if t<=r :
        
    
        if mylist != [0]:
            a.append(mylist)
            e=sum(mylist)
            y="true"
    elif t==0 :
        y="false"
    else:
        y="true"
        print "error doste xana eisodo einai lathos to sinolo ton probaton ayths tis nixtas"

g=int(raw_input("posa htan ta probata stin arxi? oeoo?"))
sub=g-e
print "ta probata poy xathikan stin teleytaia sosti katametrisi einai:",sub
