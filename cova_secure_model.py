from cova_secure_io_helpers import fetch_data_s3, persist_model
from cova_secure_model_helpers import extract_model_params

class CovaSecureModel(object):
    """docstring for CovaSecureModel"""
    def __init__(self, data_hash, X_feats, Y_feats=None, 
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
        self.YY = 

    def check_information_amount(self):

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
        self.model_params = 

    def extract_model_params(self):
        persist_model(self.model_params, self.model_scores)


    def run(self):
        self.fetch_data_local()
        self.process_data()
        self.train_model()


if __name__ == '__main__':
    main()