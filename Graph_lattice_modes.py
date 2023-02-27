#Graphite Frequencies 
#Siebentritt et.al 1997 at K point
#Aizawa et.al 1990      at T,M point

a_s = 0 ; a_0 = 1.42E-10 ; a_1 = 364 ; a_2 =  62
y_1 = 8.30E-19; y_2 = 3.38E-19
m   = 12*1.66E-27;delta = 3.17E-19
def Graphite_K(a_s,a_0,a_1,a_2,y_1,y_2,m,delta):   #Siebentritt et.al 1996
#ZA/ZO mode
  w12  = ((2*a_s+((3*delta)/(a_0*a_0))+((9*y_2)/(a_0**2)))*(1/m))**(0.5)
#SH mode
  w3   =  ((1/(2*m))*((9*a_2)+((36*y_1)/(a_0**2))))**(0.5)
#LO/LA mode
  w45  = ((1/(2*m))*((3*a_1)+(9*a_2)+((9*y_1)/(a_0**2))))**(0.5)
  w6   =  ((1/(2*m))*((6*a_1)+(9*a_2)))**(0.5)
  print("Siebentritt et.al K")
  print("ZA,ZO =","{:e}".format(w12))
  print("SH    =","{:e}".format(w3))
  print("LO    =","{:e}".format(w45))
  print("LA    =","{:e}".format(w6))
  print("")

def Graphite_TM(a_s,a_0,a_1,a_2,y_1,y_2,m,delta):      #Aizawa et.al 1990
#ZA_M
  w_ZAM = ((((12*y_2)/(a_0**2))+((16*delta)/(a_0**2))*(1/m)))**(0.5)
#ZA_T
  w_ZAT = (a_s/m)**(0.5)
#ZO_T
  w_ZOT = ((((108*y_2)/(a_0**2))+(a_s))*(1/m))**(0.5)
#ZO_M
  w_ZOM = ((((48*y_2)/(a_0**2))+(a_s))*(1/m))**(0.5)
  print("Aizawa et.al M")
  print("ZA,T =","{:e}".format(w_ZAT))
  print("ZA,M =","{:e}".format(w_ZAM))
  print("ZO,T =","{:e}".format(w_ZOT))
  print("ZO,M =","{:e}".format(w_ZOM))
  print("")
Graphite_K(0,1.42E-10,344,62,9.30E-19,3.08E-19,12*1.66E-27,4.17E-19) # Siebentritt et. al 1996
Graphite_K(0,1.42E-10,364,62,8.30E-19,3.38E-19,12*1.66E-27,3.17E-19) # Aizawa et.al 1990
Graphite_TM(0,1.42E-10,364,62,8.30E-19,3.38E-19,12*1.66E-27,3.17E-19)
