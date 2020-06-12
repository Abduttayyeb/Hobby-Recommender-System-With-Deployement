from flask import Flask
from flask import request,url_for,redirect,render_template
app = Flask(__name__)
from sklearn.preprocessing import Normalizer
import numpy as np
import pickle

model=pickle.load(open("pickle_model_SVM.pkl","rb"))

@app.route("/")
def home():
     return render_template("form.html")

@app.route("/predict",methods=["POST"])
def predict():

    input_val = [i for i in request.form.values()]
    uncat=input_val[10:13]
    Normalized= Normalizer().fit_transform(np.array(uncat).reshape(-1,1))
    features= [j for j in input_val[0:10]]
    features_encode=[]
    for z in features:
        if z=="Yes":
            features_encode.append(1)
        elif z=="No":
            features_encode.append(0)
        elif z=="Mathematics":
            features_encode.append(2)
        elif z=="Science":
            features_encode.append(3)
        elif z=="Any Language":
            features_encode.append(0)
        elif z=="History/Geography":
            features_encode.append(1)
    for k in Normalized :
        features_encode.append(int(k))
    prediction = model.predict(np.array(features_encode).reshape(1,-1))
    if int(prediction)==0:
        prediction = "Predcited Hobby : Academics "
    elif int(prediction)==1:
        prediction = "Predicted Hobby : Arts"
    elif int(prediction)==2:
        prediction = "Predicted Hobby : Sports"
    return render_template("result.html",features_encode=features_encode,prediction =prediction)


if __name__=='__main__':
    app.run(debug=True)