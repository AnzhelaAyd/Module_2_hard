a = int(input('chislo a= '))
k=''
for i in range(1, a):
   for j in range(2, a):
       if j<=i:
            continue
     if a % (i+j)==0:
          k = str(i)+str(j)
print (k)
