#-------------------------------------------------------------------------------
# Name:        Discrete Charge E-Field Calculator
# Purpose: This program is designed to calculate the electrostatic field
#by asking the user for the positions and charges of each particle,
#then for the position and charge of the test charge. Language - Python
#-------------------------------------------------------------------------------

from math import *

def main():
    n=1
    x=[]
    y=[]
    theta=[]
    x_hat=[]
    y_hat=[]
    particles=float(input("number of particles: "))
    X=float(input("Test x-coordinate: "))
    Y=float(input("Test y-coordinate: "))
    while(n<=particles):
        q=float(input("Particle #"+str(n)+" charge: "))
        m=float(input("Particle #"+str(n)+" x-coordinate: "))-X
        v=(float(input("Particle #"+str(n)+" y-coordinate: "))-Y)
        if(m==0):
            Abs=0
        else:
            Abs=q /(m**2 + v**2)
            theta=tan(v/m)
            x_hat.append(Abs*cos(theta))
            y_hat.append(Abs*sin(theta))
            x.append(Abs)
        n+=1
    e=4*pi*8.22e-12
    print("Magnetude of Electric Field = "+str(sum(x)/e)+" (kg*m)/(s^3*A)")
    print("<"+str(sum(x_hat)/e)+","+str(sum(y_hat)/e)+">"+" (kg*m)/(s^3*A)")

print("The following program calculates the electric field at discrete "+
      "points based on the location and charges of user-defined test "+
      "particles \n")
print(main())
