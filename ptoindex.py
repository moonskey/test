const = [0,1,2,6,24,120,720,5040,40320,362800,3628000,39908000,478896000,6225648000,87159072000,1307386080000,20918177280000,355609013760000,6400962247680000,121618282705920000,2432365654118400000]
def ptoindex(n,type,s):
    ls = ['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n']
    lsn = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n']
    num = range(n)
    index = 0
    idx = ''
    if(type=="dic"):
        for i in range(n):       
            num[i] = 0
            for j in range(i+1,n):
                if(s[i]>s[j]):
                    num[i]=num[i]+1
            index = index + num[i]*const[n-i-1]
        for i in range(0,n-1):
            idx = idx + lsn[num[i]]
    if(type=="inc"):
        for i in range(n):
            ss = s[i]
            val = n - lsn.index(ss)
            num[val] = 0
            for j in range(i+1,n):
                if(s[i]>s[j]) : num[val]=num[val]+1
            index = index + num[val]*const[n-val-1]
        for i in range(0,n-1):
            idx = idx + lsn[num[i]]
    if(type=="dec"):
         for i in range(n):
            ss = s[i]
            val = n - lsn.index(ss)
            num[val] = 0
            for j in range(i+1,n):
                if(s[i]>s[j]) : num[val]=num[val]+1       
         for j in range(0,n-1):
            index = index*(j+2)+num[j+1]
         for i in range(n-2,-1,-1):
            idx = idx + lsn[num[i]]
    if(type=="switch"):
         for i in range(n):
            num[i] = 0
         num[1] = 1
         for j in range(2,n):
            ##val = s.find(str(j+1))
            val = s.find(ls[j])
            if(j%2==0):
                if(num[j-1]%2==0):
                    for k in range(val+1,n):
                        if(s[k]<s[val]): num[j]=num[j]+1
                if(num[j-1]%2==1):
                    for k in range(0,val):
                        if(s[k]<s[val]): num[j]=num[j]+1
            if(j%2==1):
                if((num[j-2]+num[j-1])%2==0):
                    for k in range(val+1,n):
                        if(s[k]<s[val]): num[j]=num[j]+1
                if((num[j-2]+num[j-1])%2==1):
                    for k in range(0,val):
                        if(s[k]<s[val]): num[j]=num[j]+1
         for j in range(0,n-1):
            index = index*(j+2)+num[j+1]
         for i in range(1,n):
            idx = idx + lsn[num[i]]
    #print num
    return index,idx

print ptoindex(8,'dic','83674521')
print ptoindex(15,'dic','fedcba987654321')
print ptoindex(8,'dic','85237614')
print ptoindex(8,'inc','83674521')
print ptoindex(8,'inc','87543126')
print ptoindex(8,'dec','83674521')
print ptoindex(8,'dec','47683215')
print ptoindex(8,'switch','83674521')
print ptoindex(8,'switch','32741865')
