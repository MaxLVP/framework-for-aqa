import logging
from utilsclasses.config_manager import WorkingWithData


class Logging:

    logger = logging.getLogger("loger")
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(WorkingWithData.working_with_data("format", "logger_config"))
    fh = logging.FileHandler(WorkingWithData.working_with_data("filename", "logger_config"), WorkingWithData.working_with_data("read_mode", "logger_config"))
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    @staticmethod
    def write_log_info(msg, logger=logger):
        logger.info(msg)

    @staticmethod
    def write_log_debug(msg, logger=logger):
        logger.debug(msg)
