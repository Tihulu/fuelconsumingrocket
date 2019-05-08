def sort(x):
	l=len(x)
	i=l-1
	while i>0:
		for j in range (0,i):
	 		if x[j]>x[j+1]:
	 			a=x[j]
	 			b=x[j+1]
	 			x[j]=b
	 			x[j+1]=a
		i=i-1
	print(x)
	return x

file1 = open("unsorted.dat","r")
x=[]
for line in file1:
	a=line.split()
	b=float(a[0])
	x.append(b)

sort=sort(x)
print(sort)
l=len(sort)
file2 = open("sorted.txt","w")
for q in range (0,l):
	file2.write(str(sort[q]))
	file2.write("\n")
