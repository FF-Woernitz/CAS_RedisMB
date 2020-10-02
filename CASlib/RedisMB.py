import redis, os, json
from . import Logger

class RedisMB():
    def __init__(self, data = None):
        self.logger = Logger.Logger(self.__class__.__name__).getLogger()

        if data is not None:
            host = data["REDIS_HOST"]
            port = data["REDIS_PORT"]
            db = data["REDIS_DB"]
        else:
            host = os.getenv('REDIS_HOST', '127.0.0.1')
            port = os.getenv('REDIS_PORT', 6379)
            db = os.getenv('REDIS_DB', 0)
        self.logger.info("Connecting to Redis DB on {}:{} DB: {}".format(host, port, db))
        self.r = redis.Redis(host, port=port, db=db, health_check_interval=15, socket_connect_timeout=10)
        self.p = self.r.pubsub()
        self.subthread = None

        self.r.ping()

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
    def subscribeToType(self, type, callback):
        self.p.subscribe(**{type: callback})
        if self.subthread is None:
            self.subthread = self.p.run_in_thread(sleep_time=0.01)
        return self.subthread