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
            host = data["REDIS_HOST"]
            port = data["REDIS_PORT"]
            db = data["REDIS_DB"]
        else:
            host = os.getenv('REDIS_HOST', '127.0.0.1')
            port = os.getenv('REDIS_PORT', 6379)
            db = os.getenv('REDIS_DB', 0)
        print("Connect to Redis DB on {}:{} DB: {}".format(host, port, db))
        self.r = redis.Redis(host, port=port, db=db)
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










