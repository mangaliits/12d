import math
kmg=float(input("ievadi kvadrāta malas garumu: "))
i=5
if kmg<5:
  print("neeeeeee, neder. mazins kvadratins")
else:
  kvl= math.pow(kmg,2)
  print("kvadrata laukums:", kvl)
  newkv=kmg+5
  newkvl= math.pow(newkv,2)
  print("jaunā kv lauk.: ", newkvl)
print("jaunais kv palielinajās par:", round((newkvl*100/kvl) -100), "%")
print("\n")


from math import pi as pi
import math
rr=float(input("ievadi riņķa rādiusu: "))
hip=float(input("vienādsānu taisnleņķa trijstūra hipotenūzas garumu: "))

rlauk= pi*math.pow(rr,2)
print("riņķa laukums ir: ", round(rlauk,2))
h= hip/2
trlauk= h*hip/2
print("trijstura laukums ir: ", trlauk)

print("riņķa laukums ir lielāks par: ", round(rlauk-trlauk,1), "cm")
