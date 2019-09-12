from _datetime import datetime


class loggerFile:
    instance = None
    base_path = "/home/ec2-user/workspace/nurvey-python/"
    base_path2 = "/home/nurveyneural/Documentos/NURVEYDEV/nurvey-python/"

    def __init__(self):
        self.name = "logger"
        self.fileName = self.base_path + "log-"+datetime.now().strftime("%m-%d-%Y") + ".txt"

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = loggerFile()
        return cls.instance

    def appendLog(self, log):
        the_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S.%f")

        f = open(self.fileName, "a+")
        f.write(the_time + " - " + log + " \n")
        f.close()

    def INFO(self, info):
        self.appendLog("INFO - " + info)

    def DEBUG(self, debug):
        self.appendLog("DEBUG - " + debug)

    def OUTPUT(self, output):
        self.appendLog("OUTPUT - " + output)

    def INPUT(self, input):
        self.appendLog("INPUT - " + input)


loggerFile = loggerFile.get_instance()
