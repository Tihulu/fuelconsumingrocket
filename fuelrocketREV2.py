
											#theoretical background#

						#details for thrust
	#Thrust=(exhaust velocity)*(dmass/dtime)
		#https://www.wikiwand.com/en/Thrust

						#details for escape velocity and orbit velocity
	#(escape velocity) = sqrt(((2*Gr*Me)/(R+x)))
	#(orbit velocity) = sqrt(((Gr*Me)/(R+x)))
		#http://hyperphysics.phy-astr.gsu.edu/hbase/vesc.html

						#details for drag force
	#Air friction force = (1/2)*dc*density*A*(v^2)
	#air density = pressure/(specific gas constant*Temp)   (ideal gas law)
	#Dc = 0.5  #drag coeff of cone
	#Gc = 287.058 #specific gas constant
	#Pa = 101325 (Pa equals to 1 atm)
	#ad = 1.225 kg/m^3 #air density initially in 1atm (101325 Pa) in 15*C (ISA standards)
	#dT= -0.0065 #change in temperature in height (Kelvin)/(meter height) (assumed that it is linear)
	#dP= -(air density)*(acceleration of gravity) (Pascal pressure change per meter)
		#https://www.wikiwand.com/en/International_Standard_Atmosphere
		#https://www.wikiwand.com/en/Density_of_air
		#https://www.wikiwand.com/en/Vertical_pressure_variation

#libraries that we needed to plot
import numpy as np
import math as m
import matplotlib.pyplot as plot
import sys
import xlsxwriter #https://www.geeksforgeeks.org/python-create-and-write-on-excel-file-using-xlsxwriter-module/
#											functions
def drag_force(x,ya,Gr,Me,R,ad,Dc,A,v):
	if x<ya:
		dT= (-0.0065)*x #change in temperature in height (Kelvin)/(meter height) (assumed that it is linear)
		Temp=273.15+15+dT #Temp. in Kelvin
		Gc = 287.058 #specific gas constant
		grav_acc = (Gr*Me)/((R+x)**2) #acceleration of gravity
		dP = (-1)*(ad)*(grav_acc)*x  #(in Pascal) pressure change per meter)
		P = 101325+dP #(Pressure in pascal)
		ad = P/(Gc*Temp) #(ideal gas law)
		fdrag = -0.5*Dc*ad*A*(v*(abs(v))) #Air friction force
		return fdrag
	else:
		fdrag=0
		return fdrag

def write_to_file(time,d,sp):
	xlsx= xlsxwriter.Workbook('time_distance_velocity.xlsx') #to write excel file (needs library xlsxwriter)
	data = xlsx.add_worksheet()
	data.write('A1', 'Time (s)')
	data.write('B1', 'Distance (m)')
	data.write('C1', 'Velocity (m/s)')

	txt=open("time_distance_velocity.txt","w") #to write txt file	
	txt.write('{:s} 	{:s} 	{:s}'.format("Time (s)","Distance (m)","Velocity (m/s)"))
	txt.write("\n")

	for i in range(len(sp)):
		x= time[i]
		y= d[i]
		z= sp[i]
		a='A'+str(i+2)
		b='B'+str(i+2)
		c='C'+str(i+2)
		data.write(a,str(x))
		data.write(b,str(y))
		data.write(c,str(z))
		write=txt.write('{:f} 	{:f} 	{:f}'.format(x,y,z))
		txt.write("\n")
	txt.close()
	xlsx.close()


def plot_graph(time,d,sp): #(needs library matplotlib and numpy)
	#plot distance time
	plot.title('Distance vs Time')
	plot.xlabel('Time (s)')
	plot.ylabel('Distance (m) ')
	plot.plot(time, d, marker='.', color='r', linestyle='-')
	#plot.plot(time, sp, marker='.', color='g', linestyle='-')
	plot.grid(True)
	plot.savefig('RocketDvsT.png')
	plot.savefig('RocketDvsT.pdf')
	plot.show()

	#plot speed time
	plot.title('Speed vs Time')
	plot.xlabel('Time (s)')
	plot.ylabel('Speed (m/s) ')
	plot.plot(time, sp, marker='.', color='g', linestyle='-')
	plot.grid(True)
	plot.savefig('RocketSvsT.png')
	plot.savefig('RocketSvsT.pdf')
	plot.show()

									#main code

#constants in the equations
R=6378000 #Radius of the Earth
Gr=6.67*(m.pow(10,(-11))) #Gravitational constant G
Me=5.976*(m.pow(10,24)) #Mass of the Earth
ev=11200 #escape velocity
ya=11000 #the distance from the ground where oxygen ends. (in other words where engine stops)
Dc = 0.5 #drag coeff of cone
ad = 1.225 #(in kg/m^3) air density initially in 1atm (101325 Pa) in 15*C (ISA standards)
pi = m.pi

#inputs
fm = float(input("Fuel Mass in kg :"))
m = float(input("Inital Mass in kg :"))
rocketradius = float(input("Radius of the rocket in m :"))
exv = float(input("Exhaust velocity in m/s :"))
fc = float(input("Fuel consumption rate in kg/s :"))
dt = float(input("dt in seconds:"))

if (fm <= 0) or (fm >= m) or (rocketradius < 0) or (exv <= 0) or (fc <= 0) or (dt <= 0):
        print ("invalid inputs")
        sys.exit()

ff = exv*fc #the force that provided by the engine (Thrust)
A = (pi)*(rocketradius**2) #cross-sectional area in m^2

#initials
v = 0.00 #velocity
x = 0.00 #distance
a = 0.00 #acceleration
tfc=0.00 #total fuel consumption
t=0.00 #Time
vo=0.00 #orbital velocity
time = [] #array time by dt
d = [] #array distance by dt
sp= [] #array speed by dt

while 1<2: #true statement needed
	if (x<ya) and (fm>0) : #where engine is functioning
		t = t + dt
		q = fc*dt
		m = m-q
		fm = fm-q
		tfc = tfc+q
		fg = (-Gr*Me*m)/((R+x)**2)

		fdrag=drag_force(x,ya,Gr,Me,R,ad,Dc,A,v)
		if (fdrag)<0:
			if abs(fdrag)>abs(ff+fg):
				f=0
			else:
				f = ff+fg+fdrag
		if (fdrag)>0:
			if fdrag>(-fg):
				f=0
			else:
				f=ff+fg+fdrag
		if (fdrag==0):
			f=ff+fg
		a = f/m
		dv = a*dt
		v = v+dv
		dx = v*dt
		x = x+dx

		if x<0:
        #there cannot be minus distance therefore it stands on the ground
			x1=0
			s=0
			d.append(x1)
			time.append(t)
			sp.append(s)
		else: #else
			d.append(x)
			time.append(t)
			sp.append(v)

	if not v==0:
		if ((((abs(v)/v)*(v**2))==((Gr*Me*m)/(R+x))) and (dv==0)) and (x>ya):
		#the velocity is equal with the orbit velocity where there is no change in velocity and where the engine is not functioning (no oxygen)
			vo=v/(m.sqrt(2))
			print ("it's in orbit with the speed of" , vo ,"m/S","altitude of",x,"m")
			break
		if (((abs(v)/v)*(v**2))>=((2*Gr*Me)/(R+x))) and (x>ya) :
		#where the velocity is as same as or higher than the escape velocity
			print ("it will escape from The Earth (above the atmosphere) with the speed of", v ,"m/s","with the altitude of",x,"m")
			break

	if (((fm<=0.0) or (x>ya)) and (((abs(v)/v)*(v**2))<((2*Gr*Me)/(R+x)))) :
	#When the engine is not working and the rocket connot reach the escape velocity
		t = t + dt
		fg = (-Gr*Me*m)/((R+x)**2)
		fdrag=drag_force(x,ya,Gr,Me,R,ad,Dc,A,v)
		if (fdrag)>0:
			if fdrag>(-fg):
				f=0
			else:
				f=fg+fdrag
		if (fdrag)<0:
			if abs(fdrag)>abs(ff+fg):
				f=0
			else:
				f=fg+fdrag
		if (fdrag==0):
			f=fg
		a = f/m
		dv = a*dt
		v = v+dv
		dx = v*dt
		x = x+dx

		if x<0: #there cannot be minus distance therefore it stands on the ground
			x1=0
			s=0
			d.append(x1)
			time.append(t)
			sp.append(s)

		else:
			d.append(x)
			time.append(t)
			sp.append(v)



	if (fm<=0.0) and (x<=0.0) :
	#when the rocket is out of fuel and it stays on the ground
		print ("not gonna fly anymore")
		break

write_to_file(time,d,sp)
plot_graph(time,d,sp)

