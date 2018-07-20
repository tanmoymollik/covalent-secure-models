from cova_secure_io_helpers import fetch_data_s3, persist_model
from cova_secure_model_helpers import *
from cova_secure_model_const import MODEL_IMPORT_MAPS as ModelMap
from sklearn.metrics import mean_absolute_error 

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

    def prepare_model(self):
        self.model = get_model_from_params(model_name, model_params)

    def train_model(self):
        if self.model_type == 'supervised':
            self.model.fit(self.XX, self.YY)
        else:
            self.model.fit(self.XX)

    def compute_model_scores(self):
        # compute various model goodness score such as mean absolute error and so on 
        scores = 0.0

        if ModelMap[self.model]["supervised"] == 1:
            if ModelMap[self.model]["regression"] == 1:
                # computing scores for regression model

                y_predict = self.model.predict(self.X_feats)
                scores = mean_absolute_error(self.Y_feats,y_predict,multioutput='uniform_average')

            else:
                # computing scores for classification models

                y_predict = self.model.predict(self.X_feats)
                length = len(y_predict)
                total_correct = 0 

                for i in range(length):
                    if y_predict[i] == self.Y_feats[i] :
                        total_correct += 1
                
                if length != 0 :
                    scores = total_correct/length
        
        else:
            # computing scores for clustering

            scores = None

        self.model_scores = {'mae': scores}

    def check_information_ratio(self):
        # TODO: check the information ratio of input data and output params
        pass

    def secure_store_model_params(self):
        persist_model(self.model, self.model_scores)

    def run(self):
        self.fetch_data_s3()
        self.process_data()
        self.check_information_amount()
        self.prepare_model()
        self.train_model()
        self.compute_model_scores()
        self.check_information_ratio()
        self.secure_store_model_params()


if __name__ == '__main__':
    # TODO: argparse args
    cova_secure_model = CovaSecureModel()