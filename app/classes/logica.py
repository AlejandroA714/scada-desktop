import requests, json, os
from classes.logger import Logger

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
    def LeerConfiguracion():
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

    

