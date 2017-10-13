import openaq 


town1=raw_input("Give me first town name: ")
town2=raw_input("Give me second town name: ")
api=openaq.OpenAQ()

parameters=['pm25', 'pm10']
pm=[]

try:
    for i in range(len(parameters)):
        status, city1r=api.measurements(city=town1,parameter=parameters[i])
        status1, city2r= api.measurements(city=town2,parameter=parameters[i])
        if (status==200 and len(city1r['results'])!=0):
            pm.append(city1r['results'][:1][0]['value'])
            town1F=False
        else:
            town1F=True
        if (status1==200 and len(city2r['results'])!=0):
            pm.append(city2r['results'][:1][0]['value'])
            town2F=False
        else:
            town2F=True
except Exception as e:
    print e

if len(pm) == 4:
    print "pm25 measurement for city "+town1+" is: "+str(pm[0])
    print "pm10 measurement for city "+town1+" is: "+str(pm[2])
    print "pm25 measurement for city "+town2+" is: "+str(pm[1])
    print "pm10 measurement for city "+town2+" is: "+str(pm[3])
elif len(pm)==2:
    if town1F == True:
            print "City "+town1+" doesn't have any measurements"
            print "pm25 for city "+town2+" is "+str(pm[0])
            print "pm10 for city "+town2+" is "+str(pm[1])
    else:
            print "City "+town2+" doesn't have any measurements"
            print "pm25 for city "+town1+" is "+str(pm[0])
            print "pm10 for city "+town1+" is "+str(pm[1])

