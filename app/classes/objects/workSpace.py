import json, pymongo
from uuid import UUID
from pymongo.collection import ObjectId

class workSpace(object):

    def __init__( self, dict ): # Devices property must assign manually no by dict
        self.id = dict["Id"]
        self.nombre = dict["Nombre"]
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
        return  {
                 "Id":self.id,
                 "Nombre":self.nombre,
                 "Drivers":self.devices,
                 "DriversCount":self.devicesCount
                }

class device(object):

    def __init__( self, dict ):
        self.unicID = dict["UnicID"]
        self.nombre = dict["Nombre"]
        self.empty = False
        self.time = dict["Time"]
        self.x = dict["X"]
        self.y = dict["Y"]
        self.id = dict["ID"]
        self.token = dict["Token"]
        self.image = dict["Image"]
        self.lastUpdate = dict["LastUpdate"]
        
    @property
    def unicID(self):
        return self.__unicID

    @unicID.setter
    def unicID(self,value:str):
        try:
            (UUID(value))
        except ValueError:
            raise ValueError("value is not a valid GUIID")
        self.__unicID = value

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,value:str):
        if len(value) < 3:
            raise ValueError("name cannot be an empty string")
        self.__nombre = value

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self,value):
        if (value < 0 or value > 999):
            raise ValueError("time cannot be lower than 0 or greater than 999")
        self.__time = value
    
    @property
    def empty(self):
        return self.__empty

    @empty.setter
    def empty(self,value):
        self.__empty = value

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self,value:int):
        if value < 0:
            raise ValueError("x coordinate cannot be negative")
        self.__x = value
    
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self,value:int):
        if value < 0 : 
            raise ValueError("y coordinate cannot be negative")
        self.__y = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self,value):
        if len(value) < 3:
            raise ValueError("ID cannot be empty")
        self.__id = value

    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self,value):
        if len(value) < 3:
            raise ValueError("Token cannot be empty")
        self.__token = value

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self,value):
        self.__image = value

    @property
    def variables(self):
        return self.__variables

    @variables.setter
    def variables(self,value):
        self.__variables = value

    @property
    def lastUpdate(self):
        return self.__lastUpdate

    @lastUpdate.setter
    def lastUpdate(self,value):
        self.__lastUpdate = value

    def toJSON(self):
        return {
            "UnicID":self.unicID,
            "Nombre":self.nombre,
            "IsEmpty":False,
            "Time":self.time,
            "X":self.x,
            "Y":self.y,
            "ID":self.id,
            "Token":self.token,
            "Image":self.image,
            "variables":self.variables,
            "LastUpdate":self.lastUpdate
        }

class variable(object):

    def __init__(self, dict):
        self.unicID = dict["UnicID"]
        self.nombre = dict["Nombre"]
        self.pin = dict["PIN"]
        self.value = dict["Valor"]
        self.analogic = dict["Analogic"]
        self.displayColor = dict["DisplayColor"]
        self.expresion = dict["Expresion"]
        self.notify = dict["Notificar"]
        self.nivel = dict["Nivel"]
        self.output = dict["IsOutput"]

    @property
    def unicID(self):
        return self.__unicID

    @unicID.setter
    def unicID(self,value):
        self.__unicID = value

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,value):
        self.__nombre = value

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self,value):
        self.__pin = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self,value):
        self.__value = value

    @property
    def analogic(self):
        return self.__analogic

    @analogic.setter
    def analogic(self,value):
        self.__analogic = value
    
    @property
    def displayColor(self):
        return self.__displayColor

    @displayColor.setter
    def displayColor(self,value):
        self.__displayColor = value
    
    @property
    def expresion(self):
        return self.__expresion

    @expresion.setter
    def expresion(self,value):
        self.__expresion = value

    @property
    def notify(self):
        return self.__notify

    @notify.setter
    def notify(self,value):
        self.__notify = value

    @property
    def nivel(self):
        return self.__nivel

    @nivel.setter
    def nivel(self,value):
        self.__nivel = value

    @property
    def output(self):
        return self.__output

    @output.setter
    def output(self,value):
        self.__output = value

    def toJSON(self):
        return {
                "UnicID":self.unicID,
                "Nombre":self.nombre,
                "PIN":self.pin,
                "Valor":self.value,
                "Analogic":bool(self.analogic),
                "DisplayColor":self.displayColor,
                "Expresion":self.expresion,
                "Notificar":self.notify,
                "Nivel":self.nivel,
                "IsOutput":self.output
                }
