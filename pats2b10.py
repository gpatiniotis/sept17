li=[]
d=24
max4=0
max5=0
max6=0
max7=0
for i in range(d):
    a=raw_input()
    li.append(a)
    if ( i < 6 ) :
        if (li[i]> max4):
            max4=li[i]
    elif ( i < 12 ) :
        if (li[i] > max5):
            max5=li[i]
    elif ( i < 18 ) :
        if ( li[i] > max6 ):
            max6 = li[i]
            
    else:
        if (li[i]>max7):
            max7=li[i]
print "[(4), %d ,(5), %d ,(6), %d ,(7), %d ]" %(max4,max5,max6,max7)
