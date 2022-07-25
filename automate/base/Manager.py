import logging


class LogManager:

    def __init__(self, name: str):
        """
        Object Initialization
        :param name: Name of the Application (or) use-case that we are running currently.
        """
        self.sys_name = name
        self.log_formatter = logging.Formatter("%(asctime)s [%(levelname)s] - %(message)s")
        self.logger = logging.getLogger(f"LOGGER-{name}")
        self.logger.setLevel("INFO")
        self.console_handler = logging.StreamHandler()
        self.console_handler.setFormatter(self.log_formatter)
        self.logger.addHandler(self.console_handler)
        self.__write__ = {"INFO": self.logger.info,
                          "DEBUG": self.logger.debug,
                          "WARN": self.logger.warning,
                          "ERROR": self.logger.error,
                          "CRITICAL": self.logger.critical}

    def write_log(self, method: str = "INFO"):
        """
        Writes Console Log for given write method.
        :param method: Generally it uses all the default methods supported by logger module such as below.
            - [INFO, DEBUG, WARN, ERROR, CRITICAL], Defaults to INFO.
        :return: Console logger as output.
        """
        try:
            return self.__write__[method.upper()]
        except Exception as err_desc:
            raise err_desc
