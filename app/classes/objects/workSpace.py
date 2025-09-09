import json
import logging
from uuid import UUID, uuid4

try:
    from bson.objectid import ObjectId
except Exception:
    from pymongo.collection import ObjectId  # noqa

logger = logging.getLogger(__name__)


class workSpace(object):

    def __init__(self, dict=None):
        if dict is None:
            self.id = str(ObjectId())
            self.nombre = "workSpace 1"
            self.devices = []
            self.devicesCount = 0
        else:
            self.id = dict.get("Id", str(ObjectId()))
            self.nombre = dict.get("Nombre", "workSpace 1")
            drivers = dict.get("Drivers") or []
            self.devices = list(self.devicesToList(drivers))
            self.devicesCount = len(self.devices)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value: str):
        if value is None or not ObjectId.is_valid(value):
            logger.warning(f'Id inválido "{value}", generando uno nuevo.')
            value = str(ObjectId())
        self.__id = value

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value: str):
        if value is None or len(str(value)) < 3:
            logger.error(f'Nombre inválido: «{value}», mínimo 3. Manteniendo valor previo o usando "workSpace 1".')
            value = getattr(self, "_workSpace__nombre", "workSpace 1")
        self.__nombre = value

    @property
    def devices(self):
        return self.__devices

    @devices.setter
    def devices(self, value: list):
        if value is None or not isinstance(value, list):
            logger.error('La lista de dispositivos debe ser list. Se establece [].')
            value = []
        from_types_ok = []
        for d in value:
            if not isinstance(d, device):
                try:
                    from_types_ok.append(device(d))
                except Exception as e:
                    logger.error(f"Dispositivo inválido al convertir: {e}")
            else:
                from_types_ok.append(d)
        self.__devices = from_types_ok

    @property
    def devicesCount(self):
        return self.__devicesCount

    @devicesCount.setter
    def devicesCount(self, value: int):
        try:
            v = int(value)
        except Exception:
            v = 0
        if v < 0:
            logger.error("devicesCount no puede ser negativo. Se deja en 0.")
            v = 0
        self.__devicesCount = v

    def toJSON(self):
        return {
            "Id": self.id,
            "Nombre": self.nombre,
            "Drivers": list(self.deviceToJSON()),
            "DriversCount": self.devicesCount
        }

    def deviceToJSON(self):
        for d in self.devices:
            yield d.toJSON()

    def devicesToList(self, devices):
        if not devices:
            return []
        for d in devices:
            yield device(d)


class device(object):

    def __init__(self, dict=None):
        if dict is None:
            self.unicID = str(uuid4())
            self.nombre = "dev1"
            self.empty = True
            self.time = 30
            self.x = 0
            self.y = 0
            self.id = "123456789"
            self.token = "123456789"
            self.image = DEFAULT_IMAGE_BASE64
            self.lastUpdate = "Nunca"
            self.variables = []
        else:
            d = dict
            self.unicID = d.get("UnicID", str(uuid4()))
            self.nombre = d.get("Nombre", "dev1")
            self.empty = False
            self.time = d.get("Time", 30)
            # Soportar X/x, Y/y
            self.x = d.get("X", d.get("x", 0))
            self.y = d.get("Y", d.get("y", 0))
            self.id = d.get("ID", "")
            self.token = d.get("Token", "")
            self.image = d.get("Image", DEFAULT_IMAGE_BASE64)
            self.lastUpdate = d.get("LastUpdate", "Nunca")
            self.variables = list(self.variablesToList(d.get("Variables", [])))

    @property
    def unicID(self):
        return self.__unicID

    @unicID.setter
    def unicID(self, value: str):
        try:
            UUID(str(value), version=4)
        except Exception:
            logger.error(f'GUID inválido «{value}», generando uno nuevo.')
            value = str(uuid4())
        self.__unicID = value

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value: str):
        if value is None or len(str(value)) < 3:
            logger.error(f'«{value}» no es nombre válido (mín 3). Manteniendo previo o "dev1".')
            value = getattr(self, "_device__nombre", "dev1")
        self.__nombre = value

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, value):
        try:
            v = int(value)
        except Exception:
            v = 30
        if v <= 0 or v > 999:
            logger.error("Rango de tiempo admitido 1-999. Ajustando a 30.")
            v = 30
        self.__time = v

    @property
    def empty(self):
        return self.__empty

    @empty.setter
    def empty(self, value):
        self.__empty = bool(value)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value: int):
        try:
            v = int(value)
        except Exception:
            v = 0
        if v < 0:
            logger.warning("Coordenada X negativa. Ajustando a 0.")
            v = 0
        self.__x = v

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value: int):
        try:
            v = int(value)
        except Exception:
            v = 0
        if v < 0:
            logger.warning("Coordenada Y negativa. Ajustando a 0.")
            v = 0
        self.__y = v

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if value is None or len(str(value)) < 3:
            logger.error(f'ID inválido «{value}». Usando vacío.')
            value = ""
        self.__id = value

    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self, value):
        if value is None or len(str(value)) < 3:
            logger.error(f'Token inválido «{value}». Usando vacío.')
            value = ""
        self.__token = value

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, value):
        if not value:
            self.__image = DEFAULT_IMAGE_BASE64
        else:
            self.__image = value

    @property
    def variables(self):
        return self.__variables

    @variables.setter
    def variables(self, value):
        if value is None or not isinstance(value, list):
            logger.error('La lista de variables debe ser list. Se establece [].')
            value = []
        fixed = []
        for v in value:
            if not isinstance(v, variable):
                try:
                    fixed.append(variable(v))
                except Exception as e:
                    logger.error(f"Variable inválida al convertir: {e}")
            else:
                fixed.append(v)
        self.__variables = fixed

    @property
    def lastUpdate(self):
        return self.__lastUpdate

    @lastUpdate.setter
    def lastUpdate(self, value):
        if not value:
            value = "Nunca"
        self.__lastUpdate = value

    def toJSON(self):
        return {
            "UnicID": self.unicID,
            "Nombre": self.nombre,
            "IsEmpty": False,
            "Time": self.time,
            "X": self.x,
            "Y": self.y,
            "ID": self.id,
            "Token": self.token,
            "Image": self.image,
            "Variables": list(self.varToJSON()),
            "LastUpdate": self.lastUpdate
        }

    def varToJSON(self):
        for v in self.variables:
            yield v.toJSON()

    def variablesToList(self, vars):
        if not vars:
            return []
        for v in vars:
            yield variable(v)


class variable(object):

    def __init__(self, dict=None):
        if dict is None:
            self.unicID = str(uuid4())
            self.nombre = "var1"
            self.pin = "AI0"
            self.value = "0"
            self.analogic = True
            self.displayColor = None
            self.expresion = None
            self.notify = None
            self.nivel = None
            self.output = False
        else:
            d = dict
            self.unicID = d.get("UnicID", str(uuid4()))
            self.nombre = d.get("Nombre", "var1")
            self.pin = d.get("PIN", "AI0")
            self.value = d.get("Valor", "0")
            self.analogic = bool(d.get("Analogic", True))
            self.displayColor = d.get("DisplayColor")
            self.expresion = d.get("Expresion")
            self.notify = d.get("Notificar")
            self.nivel = d.get("Nivel")
            self.output = bool(d.get("IsOutput", False))

    @property
    def unicID(self):
        return self.__unicID

    @unicID.setter
    def unicID(self, value):
        try:
            UUID(str(value), version=4)
        except Exception:
            logger.error(f'GUID inválido «{value}», generando uno nuevo.')
            value = str(uuid4())
        self.__unicID = value

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        if value is None or len(str(value)) < 3:
            logger.error(f'«{value}» no es un nombre válido (mín 3). Manteniendo previo o "var1".')
            value = getattr(self, "_variable__nombre", "var1")
        self.__nombre = value

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, value):
        if not value:
            logger.error("PIN vacío/None. Manteniendo previo o 'AI0'.")
            value = getattr(self, "_variable__pin", "AI0")
        self.__pin = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def analogic(self):
        return self.__analogic

    @analogic.setter
    def analogic(self, value):
        if not isinstance(value, bool):
            logger.error('Propiedad "analogic" debe ser bool. Se fuerza a True.')
            value = True
        self.__analogic = value

    @property
    def displayColor(self):
        return self.__displayColor

    @displayColor.setter
    def displayColor(self, value):
        if value in ("", "null", None):
            self.__displayColor = None
        else:
            self.__displayColor = value

    @property
    def expresion(self):
        return self.__expresion

    @expresion.setter
    def expresion(self, value):
        """
        Convertidor: solo admite +, *, /, paréntesis, números y la variable x.
        Debe contener 'x' para tener sentido; si viene vacío o 'null' => None.
        """
        if value in ("", "null", None):
            self.__expresion = None
            return
        s = str(value).strip()
        import re
        # Solo dígitos, x, + * / . espacios y paréntesis
        if not re.fullmatch(r"[0-9x\.\s\+\*/\(\)]+", s):
            logger.error(f'Expresión inválida «{value}». Debe usar solo +,*,/ y contener x.')
            self.__expresion = None
            return
        if "x" not in s:
            logger.error(f'Expresión inválida «{value}»: no contiene x.')
            self.__expresion = None
            return
        self.__expresion = s

    @property
    def notify(self):
        return self.__notify

    @notify.setter
    def notify(self, value):
        """
        Condición para notificar. Acepta:
          - Sintaxis normal:  x < 11, x<=-3.5, x!=0, x==10, x>=2.5, x>0
          - Sintaxis legado:  x->N (>= N), x-<N (<= N)  [solo enteros en legado]
        Si es inválida, se guarda None y se loguea (no se levanta excepción).
        """
        if value in ("", "null", None):
            self.__notify = None
            return
        s = str(value).strip()
        import re
        normal = re.fullmatch(r"x\s*(<|<=|>|>=|==|!=)\s*(-?\d+(?:\.\d+)?)", s)
        legacy = re.fullmatch(r"x-\s*(<|>)\s*(\d+)", s)  # x-<N  o  x->N
        if normal:
            self.__notify = f"x{normal.group(1)}{normal.group(2)}"
            return
        if legacy:
            op = legacy.group(1)
            num = legacy.group(2)
            self.__notify = f"x>={num}" if op == ">" else f"x<={num}"
            return
        logger.error(f'«{value}» no es un comparador válido. Se deja None.')
        self.__notify = None

    @property
    def nivel(self):
        return self.__nivel

    @nivel.setter
    def nivel(self, value):
        if value in ("", "null", None):
            self.__nivel = None
            return
        v = str(value).lower()
        if v not in ("aqua", "green", "orange", "red"):
            logger.error(f'Nivel inválido «{value}». Debe ser aqua/green/orange/red.')
            self.__nivel = None
            return
        self.__nivel = v

    @property
    def output(self):
        return self.__output

    @output.setter
    def output(self, value):
        if not isinstance(value, bool):
            logger.error('Propiedad "output" solo admite booleanos. Se fuerza False.')
            value = False
        self.__output = value

    def toJSON(self):
        return {
            "UnicID": self.unicID,
            "Nombre": self.nombre,
            "PIN": self.pin,
            "Valor": self.value,
            "Analogic": bool(self.analogic),
            "DisplayColor": self.displayColor,
            "Expresion": self.expresion,
            "Notificar": self.notify,
            "Nivel": self.nivel,
            "IsOutput": self.output
        }


# ——————————————————————————————————————
# Imagen por defecto en base64 (tu cadena larga original)
DEFAULT_IMAGE_BASE64 = (
    "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"
)
