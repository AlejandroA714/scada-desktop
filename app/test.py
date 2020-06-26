from classes import reporte
from datetime import date, datetime, time

reporte1 = reporte({
            "NombreDispositivo":"Nombre",
            "NombreVariable":"Nombre",
            "Valor":126,
            "Usuario":"alejo.scada",
            "Fecha":date.today().strftime("%Y-%m-%d"),
            "Hora":time().strftime("%I:%M:%S"),
            "Condicion": "261<64",
            "Nivel":"aqua",
        })

reporte2 = reporte({
            "NombreDispositivo":"Nombre",
            "NombreVariable":"Nombre",
            "Valor":126,
            "Usuario":"alejo.scada",
            "Fecha":'2020-06-24',
            "Hora":"04:08:04",
            "Condicion": "261<64",
            "Nivel":"aqua",
        })

date.today().strftime()
# datetime.strptime(value, '%Y-%m-%d')

#2020-06-23T00:00:00.000Z
#strftime recevives a data return a string Obtener reportess
#strptime receives a strng return date object, nuevo Reporte
#2020-06-24


