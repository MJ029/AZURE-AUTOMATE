from automate.base.Manager import LogManager


class KVAuthentication(LogManager):

    def __init__(self):
        super().__init__(name="AZURE-AUTOMATE")
