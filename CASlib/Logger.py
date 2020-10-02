import logbook
from logbook import StreamHandler
import sys

class Logger():
    def __init__(self, module):
        logbook.set_datetime_format("utc")
        StreamHandler(sys.stdout).push_application()
        self.logger = logbook.Logger(module)

    def getLogger(self):
        return self.logger
