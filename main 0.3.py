def hts(a):
    x=a.split(':')
    
    return int(x[0])*3600+int(x[1])*60

def sth(a):
    h=a//3600
    m=(a%3600)//60
    if(h<10):
        h="0"+str(h)
    if(m<10):        
        m="0"+str(m)
    return str(h)+":"+str(m)

def first(a,b):
    if(hts(a[0][0]<b[0][0])):
       return(a)
    else:
        return(b)


def libre(a):
    libreT=[]
    if ((a[0][0]!="8:00") or (a[0][0]!="08:00")):
            libreT.append(["8:00",a[0][0]])
    if(len(a)>1):
                
        i=0
        while(i<=len(a)-2):
            libreT.append([a[i][1],a[i+1][0]])
            i+=1
        if (libreT[len(libreT)-1][1]!="19:00"):
            libreT.append([a[len(a)-1][1],"19:00"])
        return libreT
    else:
        return [[a[0][1],"19:00"]]




def intersect(a,b):
    if(hts(a[0])<=hts(b[0])):
        x=b[0]
    else:
        x=a[0]
    if(hts(a[1])>=hts(b[1])):
        y=b[1]
    else:
        y=a[1]
    return [x,y]



def check(a,b):
    result=[]
    
    lib1=libre(a)
    lib2=libre(b)
    """
    print("__________________________________________")
    #print(lib1)
    #print(lib2)
    print("__________________________________________")
    """
    for i in range(0,len(lib1)):
        
        
        for j in range(0,len(lib2)):
            if(hts(lib2[j][0])<hts(lib1[i][1])):
                result.append(intersect(lib2[j],lib1[i]))
    i=0
    
    while(i<len(result)):
        """
        print(i)
        print(" lowla : "+str(hts(result[i][0])))
        print(" Thenya : "+str(hts(result[i][1])))
        """
        if hts(result[i][0])>=hts(result[i][1]):
            """
            print("yes")
            print("["+str(result[i][0])+","+str(result[i][1])+"]")
            """
            result.pop(i)
        i+=1
    
            

    return result
        

        
        
b=[["8:30","9:25"],["10:00","10:45"],["12:30","12:50"],["13:00","13:30"],["14:30","15:25"],["16:00","16:45"],["17:30","17:50"],["18:00","19:30"]]
a=[["8:00","9:25"],["10:00","11:00"],["11:45","15:00"],["17:20","19:00"]]
"""  

print("__________________________________________")
print(intersect(["8:00","19:00"],["18:30","19:30"]))
print("__________________________________________")

"""
def reunion(a,b):
    
    #print(check(a,b))

    k=check(a,b)
    test=False
    i=0
    while (test==False):
        test=True            
        while(i<len(k)):
            if(hts(k[i][1])<hts(k[i][0])):
               k.pop(i)
               test=False
            i+=1
        return(k)
print(reunion(a,b))
