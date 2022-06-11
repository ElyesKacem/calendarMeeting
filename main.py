def hts(a):
    x=a.split(':')    
    return int(x[0])*3600+int(x[1])*60
"""
def sth(a):
    h=a//3600
    m=(a%3600)//60
    if(h<10):
        h="0"+str(h)
    if(m<10):        
        m="0"+str(m)
    return str(h)+":"+str(m)

"""
def libre(a):
    libreT=[]


##############################
    if(hts(a[0][0])>hts("08:00")):
        
    
    #if ((a[0][0]!="8:00") or (a[0][0]!="08:00")):
            libreT.append(["8:00",a[0][0]])

################################





            
    if(len(a)>1):
                
        i=0
        while(i<=len(a)-2):
            libreT.append([a[i][1],a[i+1][0]])
            i+=1





#####################################



        if(hts(a[len(a)-1][1])<hts("19:00")):
            
    
            
        
        #if (libreT[len(libreT)-1][1]!="19:00"):
            libreT.append([a[len(a)-1][1],"19:00"])

###################################




            
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

    



   
    for i in range(0,len(lib1)):
        
        
        for j in range(0,len(lib2)):


            if((hts(lib1[i][0])>=hts(lib2[j][1])) or ((hts(lib1[i][1])<=hts(lib2[j][0])))):
                
                pass
            else:
                if((hts(lib1[i][0])<hts(lib2[j][0]))):
                    if((hts(lib1[i][1])>hts(lib2[j][1]))):
                        result.append(lib2[j])
                        #print(result)
                    else:
                        result.append([lib2[j][0],lib1[i][1]])
                        #print(result)
                else:
                    
                    if((hts(lib1[i][1])<=hts(lib2[j][1]))):
                        result.append(lib1[i])
                        #print(result)
                    else:
                        result.append([lib1[i][0],lib2[j][1]])
                        #print(result)
                    





                
    return result
            
    
        
    
            

    return result
        
def removeOcc(a):

    test=True
    while test:
            
        if(len(a)>2):
            for i in range(0,len(a)-1):
                for j in range(i+1,len(a)):
                    #print(a[i])
                    if a[i]==a[j]:
                        a.pop(i)
                        test=False
                        break
    return a       
a=[["9:00","9:00"],["10:00","11:00"],["12:00","19:00"]]
b=[["8:30","12:00"],["13:00","19:00"]]



print(check(a,b))
#print(reunion(a,b))
#print(intersect(["8:30","9:25"],["10:00","10:45"]))
#print(removeOcc([['8:00', '8:30'], ['9:25', '10:00'], ['10:45', '12:30'], ['9:25', '10:00'], ['15:25', '16:00'], ['9:25', '10:00']]))
