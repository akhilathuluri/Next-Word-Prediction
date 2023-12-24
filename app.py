from flask import Flask, render_template, request
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

app = Flask(__name__)

# Load the tokenizer
with open("tokenizer.pkl", 'rb') as file:
    mytokenizer = pickle.load(file)

# Load the model
model = tf.keras.models.load_model("next-word.h5")

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    input_text = request.form['input_text']
    predict_next_words = int(request.form['predict_next_words'])


    for _ in range(predict_next_words):
        token_list = mytokenizer.texts_to_sequences([input_text])[0]
        token_list = pad_sequences([token_list], maxlen=model.input_shape[1], padding='pre')
        predicted = np.argmax(model.predict(token_list), axis=-1)
        
        output_word = ""
        for word, index in mytokenizer.word_index.items():
            if index == predicted[0]:
                output_word = word
                break
        
        input_text += " " + output_word

    return render_template('index.html', input_text=input_text)

if __name__ == '__main__':
    app.run(debug=True)





