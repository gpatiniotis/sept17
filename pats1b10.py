a=[]
mylist=[1]
y="true"
while y=="true":
    y="false"
    mylist = raw_input('Eisagetai tin lista me ta probata gia mia nixta(plikrologiste 0 gia na mas dosete ton arxiko arithmo probaton): ')
    mylist = [int(x) for x in mylist.split(',')]
    if mylist != [0]:
        a.append(mylist)
        e=sum(mylist)
        y="true"

g=int(raw_input("posa htan ta probata stin arxi? oeoo?"))
if e<=g:
    sub=g-e
    print "ta probata poy xathikan stin teleytaia katametrisi einai:",sub
else:
    f="true"
    
    while f=="true":
        a.pop()
        print "kati dosate lathos xanaprospathiste"
        mylist = raw_input('Eisagetai tin lista me ta probata gia tin teleytaia  nixta mono: ')
        mylist = [int(x) for x in mylist.split(',')]
        if mylist != [0]:
            a.append(mylist)
            e=sum(mylist)
            g=int(raw_input("posa htan ta probata stin arxi? oeoo?"))
            if e<=g:
                sub=g-e
                print "ta probata poy xathikan stin teleytaia katametrisi einai:",sub
                f="false"
            
        
