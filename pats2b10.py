li=[]
d=24
p=0
max4=0
max5=0
max6=0
max7=0
for i in range(d):
    p+=1
    a=int(raw_input("doste ena stoixeio apo ti lista")) 
    print "dosate to  %d stoixeio apo ti lista" %(p)
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
print "[('4:00pm', %d),('5:00pm', %d),('6:00pm', %d),('7:00pm', %d)]" %(max4 ,max5 ,max6 ,max7)
