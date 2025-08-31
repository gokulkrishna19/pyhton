d={1:"Mango",2:"Apple",3:"Banana",4:"Orange"}
print(d)
for i in d:
    print("Key=",i,"Value=",d[i])

del d[1]
print("After removing")


for k ,v in d.items():
    print("Key=",k,"Value=",v)

print(d)