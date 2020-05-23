import json
import pymongo
from pymongo.collection import ObjectId

class workSpace(object):

    def __init__( self, dict ):
        self.id = dict["Id"]
        self.nombre = dict["Nombre"]
        if "Drivers" in dict.keys() : 
            self.devices = dict["Drivers"] 
        else : 
            self.devices = None
        self.devicesCount = dict["DriversCount"]
        
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self,value:str):
        if not (ObjectId.is_valid(value)):
            raise ValueError("value is not a valid ObjectId")
        self.__id = value

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,value:str):
        if len(value) < 3:
            raise ValueError("name cannot be an empty string")
        self.__nombre = value

    @property
    def devices(self):
        return self.__devices
    
    @devices.setter
    def devices(self,value:list):
        self.__devices = value
    
    @property
    def devicesCount(self):
        return self.__devicesCount

    @devicesCount.setter
    def devicesCount(self,value:int):
        if value < 0 : 
            raise ValueError("device count cannot be negative")
        self.__devicesCount = value

    
    def toJSON(self):
        JSON = {"Id":self.id,"Nombre":self.nombre,"Drivers":self.devices,"DriversCount":self.devicesCount}
        return json.dumps(JSON)

#     public class Driver
#     {
#         public String UnicID { get; set; }
#         public String Nombre { get; set; }
#         public bool IsEmpty { get; set; }
#         public int Time { get; set; }
#         public int X { get; set; }
#         public int Y { get; set; }
#         public String ID { get; set; }
#         public String Token { get; set; }
#         public byte[] Image { get; set; }
#         public List<Variable> variables { get; set; }
#         public String LastUpdate { get; set; }
#     }
#     public class Variable
#     {
#         public String UnicID { get; set; }
#         public String Nombre { get; set; }
#         public String PIN { get; set; }
#         public String Valor { get; set; }
#         public Boolean Analogic { get; set; }
#         public String DisplayColor { get; set; }
#         public String Expresion { get; set; }
#         public String Notificar { get; set; }
#         public String Nivel { get; set; }
#         public Boolean IsOutput { get; set; }
#     }
# }