def generate_main():
    return """from sklearn.metrics import r2_score
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

from MLModelClassWrapper.IO import *
from MLModelClassWrapper.MLModel import *
import io, base64, os

def loadmodels(MY_MODELS, resource="."):
    models = {}
    for k, v in MY_MODELS.items():
        def f(path):
            return os.path.join(resource, path)
        modelfile = f(v["file"])
        X, y, ms = loaddata(f(v["test_X"]), f(v["test_y"]), mean_std_file=f(v["mean_std"]))
        models[k.replace(" ","_")] = {"model": MLModel(modelfile, scale=True, ms=ms),
                                    "X_test": X.values, "y_test": y.values, "mean_std": ms}
    return models

def single_model_predict(model, X):
    X = np.array(X)
    if len(X.shape)==2:
        pass
    else:
        X = X.reshape(1, -1)
    y_col = model["y_test"].shape[1]
    y = model["model"].predict(X).reshape(-1, y_col)
    return {"y": [y[:,i].tolist() for i in range(y_col)]}

def create_model_report(mymodel, Name):
    X = mymodel["X_test"]
    y = mymodel["y_test"]
    y_ = mymodel["model"].predict(X).reshape(y.shape)
    modeltype = str(type(mymodel["model"].model)).split("'")[1]
    R2 = r2_score(y, y_)
    my_stringIObytes = io.BytesIO()
    min_ = min(np.min(y), np.min(y_))
    max_ = max(np.max(y), np.max(y_))
    d = 0.05*(max_ - min_)
    rang = [min_-d, max_+d]
    plt.clf()
    plt.scatter(y, y_)
    plt.plot(rang, rang, ":", c='r')
    plt.xlabel("Measured values")
    plt.ylabel("Predicted values")
    plt.xlim(rang)
    plt.ylim(rang)   
    plt.axis('square')
    plt.savefig(my_stringIObytes, format='jpg')
    my_stringIObytes.seek(0)
    my_base64_jpgData = base64.b64encode(my_stringIObytes.read())
    str_ = f"{my_base64_jpgData}"[2:-1]
    return f'''<div style="text-align:center">
                Name: <b>{Name}</b><br>
                Model Type: <b>{modeltype}</b><br>
                R2: <b>{R2 :.2f}</b><br>
                <img src="data:image/png;base64, {str_}" />
                </div>'''
"""
