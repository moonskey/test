const = [0,1,2,6,24,120,720,5040,40320,362800,3628000,39908000,478896000,6225648000,87159072000,1307386080000,20918177280000,355609013760000,6400962247680000,121618282705920000,2432365654118400000]
def indextop(n,type,index):
    ls = ['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n']
    lsn = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n']
    num = range(n-1,-1,-1)
    res = range(n)
    used = range(n)
    result = ''
    idx = ''
    if(type=="dic"):
        for i in range(0,n-1):
            # num[i] = index/const[n-i-1]
            # index = index%const[n-i-1]
	    val = index/const[n-i-1]
	    num[i] = val
	    index = index%const[n-i-1]
        for i in range(0,n):
            result = result+(ls[num[i]])
            ls.remove(ls[num[i]])
	for i in range(0,n-1):
	    idx = idx + lsn[num[i]]
##        len = 0
##        for i in range(0,n):
##            for j in range(n):
##                if(num[j]-i==0):
##                    res[j] = int(ls[0])
##                    ls.remove(ls[0])
##                    if(len==n):  break
            
    if(type=="inc"):
        for i in range(0,n-1):
            num[i] = index/const[n-i-1]
            index = index%const[n-i-1]        
        pos = range(n-1,-1,-1)
        for i in range(n):
            res[pos[num[i]]]=n-i
            pos.remove(pos[num[i]])
        for i in range(n):
            result = result + lsn[res[i]]
        for i in range(0,n-1):
            idx = idx + lsn[num[i]]
            
    if(type=="dec"):
        for i in range(n):
            num[n-i-1] = index%(n-i)
            index = index/(n-i)        
        pos = range(n-1,-1,-1)
        for i in range(n):
            res[pos[num[n-1-i]]]=n-i
            pos.remove(pos[num[n-1-i]])
        for i in range(n):
            result = result + lsn[res[i]]
        for i in range(1,n):
            idx = idx + lsn[num[i]]

    if(type=="switch"):
        for i in range(n):
            res[i]=0
            num[n-i-1] = index%(n-i)
            index = index/(n-i)        
        pos = range(n-1,-1,-1)
        for i in range(n-1,1,-1):
            if(i%2==1):
                if((num[i-1]+num[i-2])%2==1):
                    res[pos[i-num[i]]]=i+1
                    pos.remove(pos[i-num[i]])
                if((num[i-1]+num[i-2])%2==0):
                    res[pos[num[i]]]=i+1
                    pos.remove(pos[num[i]])
            if(i%2==0):
                if(num[i-1]%2==1):
                    res[pos[i-num[i]]]=i+1
                    pos.remove(pos[i-num[i]])
                if(num[i-1]%2==0):
                   res[pos[num[i]]]=i+1
                   pos.remove(pos[num[i]])
            if(num[1]==0):
                res[pos[0]]=2
                res[pos[1]]=1
            if(num[1]==1):
                res[pos[0]]=1
                res[pos[1]]=2
        for i in range(1,n):
            idx = idx + lsn[num[i]]
        for i in range(n):
            result = result + lsn[res[i]]
        

            
    return idx,result

print indextop(8,'dic',37313)
print indextop(8,'dic',38326)
print indextop(8,'inc',38705)
print indextop(8,'inc',39718)
print indextop(8,'dec',37895)
print indextop(8,'dec',38908)
print indextop(8,'switch',22584)
print indextop(8,'switch',23597)
print indextop(9,'switch',203393)
        
    
