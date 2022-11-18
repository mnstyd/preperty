from cgi import test
from html.entities import html5
from operator import index
# from crypt import methods
from pyexpat import features
from flask import Flask, render_template, request
import numpy as np
import pickle
import math

app = Flask(__name__) 
# template_folder='template'
model = pickle.load(open('model/model_houseprices.pkl', 'rb'))

@app.route('/')
def main():
    return (render_template('main.html'))

@app.route("/predict", methods=['POST'])
def predict():
    features = []
    for val in request.form.values():
        features.append(val)

    # Street Test
    # Paved = 1
    # Gravel = 2

    

    house = int(features[0])
    house1 = int(features[1])
    house2 = int(features[2])
    house3 = int(features[3])
    house4 = int(features[4])
    house5 = int(features[5])
    house6 = int(features[6])
    house7 = int(features[7])
    house8 = int(features[8])
    house9 = int(features[9])



    hasil_prediksi = model.predict([[house, house1, house2, house3, house4, house5, house6, house7, house8, house9]])[0]
    hasil_prediksi_format = '{:20,.2f}'.format(round(hasil_prediksi))
    hasil_prediksi_idr = hasil_prediksi * 14685
    hasil_prediksi_idr_format = '{:20,.2f}'.format(round(hasil_prediksi_idr))
    dollar = "$"
    rupiah = "Rp"
    

    return render_template("main.html", house=house, dollar=dollar, rupiah=rupiah, hasil_usd=hasil_prediksi_format, hasil_idr = hasil_prediksi_idr_format) #[ind])

if __name__ == "__main__":
    app.run(debuh=True)