p='showkatul'
n=[]
descr=[]
c=0
for i in p:
    c=c+1
    if c<=3:
        st=ord(i)+2
        cst=chr(st)
        n.append(cst)
    else:
        st=ord(i)-2
        cst=chr(st)
        n.append(cst)

for i in n:
    print(i,end='')
print()
dc=0
for i in n:
    dc=dc+1
    if dc<=3:
        num=ord(i)-2
        str=chr(num)
        descr.append(str)
    else:
        num=ord(i)+2
        str=chr(num)
        descr.append(str)
for i in descr:
    print(i,end='')


        

    