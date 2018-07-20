from cova_secure_model_const import *

def get_secure_params(model_params):
    # check if the model params are secure to pass
    # consult the documentations

    return model_params

def get_model_from_params(model_name, model_params):
    secure_params = get_secure_params(model_params)

    try:
        s = MODEL_IMPORT_MAPS.get(model_name)
        exec('from sklearn import ' + s['import_name'])
    except Exception as e:
        raise e
    cmd = s['import_name']
    cmd += s['model_name']
    cmd += '(**secure_params)'
    return eval(cmd)
    # and so on

def extract_model_params(model, model_name):
    # find what model params we can stroe in pickle file
    
    # example 
    if model_name == 'ols':
        return model.coef_
    


