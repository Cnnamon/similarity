import json

class SimilarityConfigParser(object):
    def __init__(self):
        with open('config.json', 'r') as file:
            self.config = json.load(file)
    
    def get_train_data_folder(self):
        return self.config["train_data_folder"]

    def get_test_data_folder(self):
        return self.config["test_data_folder"]

    def get_beta(self):
        return self.config["beta"]
