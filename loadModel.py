from keras.models import model_from_json


class loadModel:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = loadModel()
        return cls.instance

    def __init__(self):
        self.loaded_model = None
        self.loadModel_fromdisk()

    def get_loadedmodel(self):
        return self.loaded_model

    def loadModel_fromdisk(self):
        json_file = open('./models/modelNoBin.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        self.loaded_model = model_from_json(loaded_model_json)
        # load weights into new model
        self.loaded_model.load_weights("./models/modelNoBin.h5")
        print("Loaded model from disk")


loadModel = loadModel.get_instance()
