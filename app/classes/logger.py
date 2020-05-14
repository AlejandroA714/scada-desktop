import os, json, logging
from logging.handlers import RotatingFileHandler

class Logger(): # Class handlee loggin from program
    
    __program_files = "/opt"
    if not os.path.exists("%s/Sistema SCADA" % __program_files): # if does not exist, is created
        os.makedirs("%s/Sistema SCADA" % __program_files)
    __log_formatter = logging.Formatter('[Desktop SCADA] [%(asctime)s] [%(levelname)s] %(message)s','%d/%m/%Y %H:%M')
    __logFile = '%s/Sistema SCADA/SCADA.log' % __program_files
    __my_handler = RotatingFileHandler(__logFile, maxBytes=5242880,
                                        backupCount=2, encoding=None, delay=0)
    __my_handler.setFormatter(__log_formatter)
    __my_handler.setLevel(logging.INFO)
    __app_log = logging.getLogger()
    __app_log.setLevel(logging.INFO)
    __app_log.addHandler(__my_handler)

    @staticmethod
    def log_error(e:Exception):
        Logger.__app_log.error("¡Error! %s" % str(e))

    @staticmethod
    def log_info(e):
        Logger.__app_log.info("¡Info! %s" % str(e))
    