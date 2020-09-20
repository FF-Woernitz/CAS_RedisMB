import redis, os, json

class LogSeverity():
    TRACE = 0
    DEBUG = 1
    INFO = 2
    WARN = 3
    ERROR = 4
    FATAL = 5


class RedisMB():
    def __init__(self, data = None):
        if data is not None:
            self.r = redis.Redis(data["redis_host"], port=data["redis_port"], db=data["redis_db"])
        else:
            self.r = redis.Redis(os.getenv('redis_host', '127.0.0.1'), port=os.getenv('redis_port', 6379),
                        db=os.getenv('redis_db', 0))
    def _publish_message(self, queue, message):
        message = json.dumps(message, separators=(',', ':'), sort_keys=True, indent=None)
        self.r.publish(queue, message)
    def exit(self):
        self.r.close()
    def newZVEI(self, zvei):
        message = {"type": "new_zvei", "zvei": zvei}
        self._publish_message("new_zvei", message)
    def errorZVEI(self, zvei):
        message = {"type": "error_zvei", "zvei": zvei}
        self._publish_message("error_zvei", message)









