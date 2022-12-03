from flask import Flask, render_template, request
import pickle

# Running the flask app
app = Flask(__name__)

# load model using pickle
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    int_feature = [int(x) for x in request.form.values()]
    prediction = model.predict([int_feature])[0]
    prediction = round(prediction, 1)

    return render_template('index.html', prediction_text='The result of the prediction is {}'.format(prediction))

if __name__ == '__main__':
    app.run(debug=True)
