import inspect
import logging
class Baseclass:
    def getlogger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        formatter = logging.Formatter("%(asctime)s : %(name)s : %(levelname)s : %(message)s")
        Filehandler = logging.FileHandler("logfile.log")
        Filehandler.setFormatter(formatter)
        logger.addHandler(Filehandler)
        logger.setLevel(logging.DEBUG)
        return logger
