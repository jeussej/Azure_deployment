import json
import numpy as np
import os
import pickle
import joblib

model_path = "./models/clf.pkl"

model = joblib.load(model_path)

# X= df[["kills", "deaths" , "goldDiff" , "expDiff"]].copy()

data = [15 , 10 , -2000 , -147]

x = np.array(data)
x = x.reshape(1, -1)

y_hat = model.predict(x)


print(y_hat)