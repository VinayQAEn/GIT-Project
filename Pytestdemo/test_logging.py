import logging


def test_loggingdemo():
    logger = logging.getLogger(__name__)
    File = logging.FileHandler("logfile.log")
    Formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    File.setFormatter(Formatter)
    logger.addHandler(File)
    logger.setLevel(logging.INFO)

    logger.debug("A debug information is executed")
    logger.info("Information statement")
    logger.warning("Something is in warning mode")
    logger.error("A major error has happened")
    logger.critical("Crictical issue")