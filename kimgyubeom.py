a=input("입력")

list=[]

d=len(a)

h=int((d*(d+1))/2)

b=0

c=1

e=1

f=1

g=1

for i in range(d) :
    for i in range(d) :
        k=a[b:c]
        list.append(k)
        b=b+e
        c=c+f
    b=0
    c=1
    c=c+g
    g=g+1
    d=d-1

k=0

print(list)

for i in range(h-1) :

    s=2

    if h==k :
        break;
   
    if int(list[k]) != s :

        int(list[k])%s
        
        if int(list[k])%s==0 :
            print(list[k], "소수가 아닙니다.")
            a=int(list[k])
            k=k+1
            a=s
            
        s=s+1
    
    print(list[k], "소수 입니다.")
    k=k+1  
