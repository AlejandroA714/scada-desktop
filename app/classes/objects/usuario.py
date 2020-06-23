class usuario(object):

    def __init__(self,dict = None):
        if dict is None:
            self.id = None
            self.nombres = None
            self.tipo = None
            self.usuario = None
            self.email = None
            self.enabled = None
            self.access_token = None
            self.refresh_token = None
        else:
            self.id = dict["Id"]
            self.nombres = dict["Nombres"]
            self.tipo = dict["Tipo"]
            self.usuario = dict["Usuario"]
            self.email = dict["Email"]
            self.enabled = dict["Enabled"]
            if "access_token" in dict:
                self.access_token = dict["access_token"]
            if "refresh_token" in dict:
                self.refresh_token = dict["refresh_token"]

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self,value):
        self.__id = value

    @property
    def nombres(self):
        return self.__nombres

    @nombres.setter
    def nombres(self,value):
        self.__nombres = value

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self,value):
        self.__tipo = value
        #raise Exception("¡Error! No se puede cambiar el tipo de usuario")

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self,value):
        self.__usuario = value

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self,value):
        self.__email = value
    
    @property
    def enabled(self):
        return self.__enabled

    @enabled.setter
    def enabled(self,value):
        self.__enabled = bool(value)

    @property
    def access_token(self):
        return self.__access_token

    @access_token.setter
    def access_token(self,value):
        self.__access_token = value
    
    @property
    def refresh_token(self):
        return self.__refresh_token

    @refresh_token.setter
    def refresh_token(self,value):
        self.__refresh_token = value
        #return Exception("¡Error! Solo se puede asignar un refresh token")
