from cova_secure_io_helpers import fetch_data_s3, persist_model
from cova_secure_model_helpers import *

class CovaSecureModel(object):
    """CovaSecureModel is a custom model wrapper for running private user model on 
    sensitive data in covalent secure servers (CS2) or CovaClave (C2)"""

    def __init__(self, data_hash, X_feats, Y_feats=[], 
        process_data_fn=lambda df: df,
        model_name='ols', model_params={}):
        super(CovaSecureModel, self).__init__()

        self.data_hash = data_hash
        self.X_feats = X_feats
        self.Y_feats = Y_feats
        self.process_data_fn = process_data_fn
        self.model = get_model_from_params(model_name, model_params)

    
    def fetch_data_s3(self):
        # fetch data from local shared docker volume
        self.df = get_data_s3(self.data_hash)

    def process_data(self):
        self.df = process_data_fn(self.df)
        
        self.XX = self.df[self.X_feats]
        self.YY = self.df[self.Y_feats]

    def check_information_amount(self):
        # TODO: measure Shannon's entropy in filtered data
        pass

    def train_model(self):
        if self.model_type == 'supervised':
            self.model.fit(self.XX, self.YY)
        else:
            self.model.fit(self.XX)

    def compute_model_scores(self):
        # compute various model goodness score such as mean absolute error and so on 
        self.model_scores = {'mae': 0.1}

    def get_model_params(self):
        # get the params we need to reconstruct models offline
        self.model_params = extract_model_params(self.model, self.model_name)

    def check_information_ratio(self):
        # TODO: check the information ratio of input data and output params
        pass

    def secure_store_model_params(self):
        persist_model(self.model_params, self.model_scores)

    def run(self):
        self.fetch_data_s3()
        self.process_data()
        self.check_information_amount()
        self.train_model()
        self.compute_model_scores()
        self.get_model_params()
        self.check_information_ratio()
        self.secure_store_model_params()


if __name__ == '__main__':
    # TODO: argparse args
    cova_secure_model = CovaSecureModel()