import json
import numpy as np
import os
import pickle
import joblib

def init():
    global model
    # AZUREML_MODEL_DIR is an environment variable created during deployment.
    # It's the path to the model folder (./azureml-models/$MODEL_NAME/$VERSION).
    # For multiple models, it points to the folder containing all deployed models (./azureml-models).
    model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'clf.pkl')
    model = joblib.load(model_path)

def run(raw_data):
    data = np.array(json.loads(raw_data)['data'])
    # Make prediction.
    
    x = np.array(data)
    x = x.reshape(1 , -1)

    y_hat = model.predict(x)
    
    if y_hat == 1 :
        return json.dumps({"Equipo Ganador" : "Azul" })
    else:
        return json.dumps({"Equipo Ganador" : "Rojo" })
        
    

