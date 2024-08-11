import inspect
import logging
class BaseClass:
    def getlogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        File = logging.FileHandler("logfile.log")
        Formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        File.setFormatter(Formatter)
        logger.addHandler(File)
        logger.setLevel(logging.DEBUG)
        return logger

