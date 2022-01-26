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