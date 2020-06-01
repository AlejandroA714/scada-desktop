from classes import workSpace, container
from bson import ObjectId


containers = dict()

#containers.append()
#containers.append(container({"tab":None,"workSpace":workSpace({"Id":ObjectId().__str__(),"Nombre":"Debug 2","Drivers":None,"DriversCount":0})}))
#containers.append(container({"tab":None,"workSpace":workSpace({"Id":ObjectId().__str__(),"Nombre":"Debug 3","Drivers":None,"DriversCount":0})}))

obj = ObjectId().__str__()
#containers["tab1"] = container({"tab":None,"workSpace":workSpace({"Id":obj,"Nombre":"Debug 1","Drivers":None,"DriversCount":0})})
#containers["tab2"] = container({"tab":None,"workSpace":workSpace({"Id":ObjectId().__str__(),"Nombre":"Debug 2","Drivers":None,"DriversCount":0})})
#containers["tab3"] = container({"tab":None,"workSpace":workSpace({"Id":ObjectId().__str__(),"Nombre":"Debug 3","Drivers":None,"DriversCount":0})})

#for x in containers.items():
#    print(x[1].nombre)

#tab = containers["tab2"].workSpace.id
print(tab)

#if obj in containers.items()[1]
#print(containers.keys())
#print(containers.items())