import urllib
from cova_secure_model_const import *

def get_s3_filepath(data_hash):
    return S3_BUCKET_PATH + data_hash + '.edat'

def get_s3_file(data_hash):
    return urllib.urlretrieve(get_s3_filepath(data_hash))

def fetch_data_s3():
    # https://askubuntu.com/questions/95920/encrypt-tar-gz-file-on-create
    file_path = get_s3_filepath(data_hash)


