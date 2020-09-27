import json


class Config():
    def __init__(self):
        try:
            with open("/opt/config.json") as config_file:
                try:
                    config = json.load(config_file)
                except Exception as e:
                    raise Exception("Failed to parse config file. {}".format(e))
                if len(config["trigger"]) == 0:
                    raise Exception("Please check config file. No trigger defined")
                self.config = config
        except OSError:
            raise Exception("Can't find config file please check mount point")

    def getConfig(self):
        return self.config
