from keras.models import model_from_json


class loadModel:
    instance = None
    base_path = "/home/nurveyneural/Documentos/NURVEYDEV/nurvey-python/"

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = loadModel()
        return cls.instance

    def __init__(self):
        print("loading1 model from instance")
        self.loaded_model = self.loadModel_fromdisk("models/modelNoBin")

        print("loading2 model from instance")
        self.loaded_model2 = self.loadModel_fromdisk("models/model")

    def get_loadedmodel(self):
        return self.loaded_model

    def get_loadedmodel2(self):
        return self.loaded_model2

    def loadModel_fromdisk(self, path_ToModel):
        json_file = open(self.base_path + path_ToModel +".json", 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        # load weights into new model
        loaded_model.load_weights(self.base_path + path_ToModel + ".h5")
        print("Loaded model from disk inside instance")

        return loaded_model


loadModel = loadModel.get_instance()
