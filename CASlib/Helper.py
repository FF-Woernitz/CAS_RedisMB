from datetime import datetime, time
from pytz import timezone


class Helper():
    def __init__(self):
        pass

    def isTestAlert(self, trigger):
        begin_time = time(trigger["testalarm"]["hour_start"], trigger["testalarm"]["minute_start"])
        end_time = time(trigger["testalarm"]["hour_end"], trigger["testalarm"]["minute_end"])
        now = datetime.now(timezone("Europe/Berlin"))
        return now.weekday() == trigger["testalarm"]["weekday"] and begin_time <= now.time() <= end_time
