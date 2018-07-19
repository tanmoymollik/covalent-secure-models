import urllib
from cova_secure_model_const import *

def get_s3_filepath(data_hash):
    return S3_BUCKET_PATH + data_hash + '.edat'

def get_s3_file(data_hash):
    return urllib.urlretrieve(get_s3_filepath(data_hash))

def fetch_data_s3():
    # https://askubuntu.com/questions/95920/encrypt-tar-gz-file-on-create
    file_path = get_s3_filepath(data_hash)

def persist_model(model_params, model_scores):
    # read about model persistence: http://scikit-learn.org/stable/modules/model_persistence.html
    from sklearn.externals import joblib
    try:
        file_path = DOCKER_VOLUME_PATH + 'persisted_model.pkl'
        joblib.dump(clf, file_path)
    except Exception as e:
        print 'could not write model files'
        raise e
    





