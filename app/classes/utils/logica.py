from classes.utils.logger import logger
from classes.objects.workSpace import workSpace,device,variable
import requests, json, os

class Logica():

    __program_files = "/opt"

    settings = { 
        "APISCADA":{
            "Host":"127.0.0.1",
            "Port":"8080"
        }
    }
    @staticmethod
    def IniciarSesion(**kwargs):
        _data = {"Usuario":kwargs["Usuario"],"Password":kwargs["Password"]}
        _answer = (requests.post("http://%s:%s/Sesion/IniciarSesion" % (Logica.settings["APISCADA"]["Host"],Logica.settings["APISCADA"]["Port"]), timeout = 45,json=_data)).json()
        return _answer

    @staticmethod
    def ObtenerProyectos(**kwargs): # returns a list with all project in database
        _headers = {'Authorization': 'Bearer ' + kwargs["access_token"]}
        result  = requests.get("http://%s:%s/Controles/MostrarTodos" % (Logica.settings["APISCADA"]["Host"],Logica.settings["APISCADA"]["Port"]), timeout = 45, headers=_headers)
        result.raise_for_status()
        _answer:workSpace = json.loads( result.content ,object_hook=workSpace)
        return _answer

    @staticmethod
    def AbrirProyecto(**kwargs):
        _headers = {'Authorization': 'Bearer ' + kwargs["access_token"]}
        result  = requests.get("http://%s:%s/Controles/Abrir/%s" % (Logica.settings["APISCADA"]["Host"],Logica.settings["APISCADA"]["Port"],kwargs["id"]), timeout = 45, headers=_headers)
        result.raise_for_status()
        drivers = []
        for x in result.json()["Drivers"]:
            dev = device(x)
            dev.variables = json.loads( json.dumps(x["variables"]), object_hook=variable )
            drivers.append(dev)
        workSpace({"Id":result.json()["Id"],"Nombre":result.json()["Nombre"], "DriversCount": len(drivers) })
        workSpace.devices = drivers
        return workSpace

    @staticmethod
    def LeerSensor(**kwargs):
        _headers = {'Authorization': 'Bearer ' + kwargs["access_token"]}
        result  = requests.post("http://%s:%s/Controles/LeerSensor/%s/%s" % (Logica.settings["APISCADA"]["Host"],Logica.settings["APISCADA"]["Port"],kwargs["ID"],kwargs["Token"]), timeout = 45,json=kwargs["data"],headers=_headers)
        result.raise_for_status()
        _answer:variable = json.loads(result.content, object_hook=variable)
        return _answer

    @staticmethod
    def ActualizarSensor(**kwargs):
        _headers = {'Authorization': 'Bearer ' + kwargs["access_token"]}
        result  = requests.post("http://%s:%s/Controles/ActualizarVariable/%s/%s" % (Logica.settings["APISCADA"]["Host"],Logica.settings["APISCADA"]["Port"],kwargs["ID"],kwargs["Token"]), timeout = 45,json=kwargs["data"],headers=_headers)
        result.raise_for_status()
        return result.json()



    @staticmethod
    def LeerConfiguracion():
        Logger = logger()
        try:
            file =  open("%s/Sistema SCADA/setting.json" % Logica.__program_files,"r")
            return json.load(file)
            file.close()
        except: # Si no existe lo crea
            settings =  {"APISCADA":{
                "Host":"127.0.0.1",
                "Port":"8080"
            }}
            file =  open("%s/Sistema SCADA/setting.json" % Logica.__program_files,"w")
            Logger.log_error( Exception("¡Error! No pudo leerse el archivo de configuracion, Generando uno nuevo"))
            file.write(json.dumps(settings))
            file.close()
            return settings

Logica.settings = Logica.LeerConfiguracion()

    

