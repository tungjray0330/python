num=input("Enter a number=")
print()
intnum=int(float(num))
floatnum=float(num)-intnum
intlist=[]
floatlist=[]
while intnum>0:
    if intnum%2==0:
        intlist.append(0)
        intnum=intnum/2
    if intnum%2==1:
        intlist.append(1)
        intnum=(intnum-1)/2
intlist.reverse()
while floatnum!=0:
    if floatnum*2<1:
        floatlist.append(0)
        floatnum=floatnum*2
    if floatnum*2>=1:
        floatlist.append(1)
        floatnum=floatnum*2-1
intstr="".join(str(i) for i in intlist)
floatstr="".join(str(i) for i in floatlist)
print(intstr+"."+floatstr)