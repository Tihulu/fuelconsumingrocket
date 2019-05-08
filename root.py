import math as m
import sys
def find_roots(a,b,c):
	delta=(b**2)-(4*a*c)
	if delta>0 :
		x1=(-b-(m.sqrt(delta)))/(2*a)
		x2=(-b+(m.sqrt(delta)))/(2*a)
		print("The roots are real: ",x1," and ",x2)
	if delta<0 :
		xr=((-b)/(2*a))
		xi=(m.sqrt(-delta))/(2*a)
		print("The roots are imaginary: ",xr,"+i",xi," and ",xr,"-i",xi)
	if (not delta>0) and (not delta<0):
		x=(-b)/(2*a)
		print("There is a single real root: ",x)

while True:
	numsstring = input("Enter three integers or real numbers (separate them with commas, q for quit): ")
	count  = numsstring.split(",")

	if (count[0]=='q'):
		sys.exit()
	if (len(count)>3) or (len(count)<3) :
		print("You must enter three integers. Try again.")
	if (len(count)==3) and ((not (float(count[0]))>0) and (not (float(count[0]))<0)):
		print("Not a quadratic polynomial. Try again.")
	if (len(count)==3) and ((float(count[0])>0) or (float(count[0])<0)):
		q=count[0]
		w=count[1]
		e=count[2]
		a=float(q)
		b=float(w)
		if w=='0':
			b=0
		c=float(e)
		if e=='0':
			c=0
		find_roots(a,b,c)