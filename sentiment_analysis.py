from pandas import read_csv
from numpy import array, argmax

import tensorflow.keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model

train_data = read_csv("./static/assets/dataset/updated_product_dataset.csv")    
training_sentences = []

for i in range(len(train_data)):
    sentence = train_data.loc[i, "Text"]
    training_sentences.append(sentence)

model = load_model("./static/assets/model/Text_Emotion.h5")

vocab_size = 40000
max_length = 100
trunc_type = "post"
padding_type = "post"
oov_tok = "<OOV>"

tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_tok)
tokenizer.fit_on_texts(training_sentences)

emo_code_url = {
    "Neutral": [0, "./static/assets/emoticons/neutral.png"],
    "Positive": [1,"./static/assets/emoticons/positive.png" ],
    "Negative": [2, "./static/assets/emoticons/negative.png"]
}

def predict(text):
    predicted_emotion=""
    predicted_emotion_img_url=""
    
    if  text != "":
        sentence = []
        sentence.append(text)
        sequences = tokenizer.texts_to_sequences(sentence)
        padded = pad_sequences(
            sequences,
            maxlen=max_length,
            padding=padding_type,
            truncating=trunc_type
        )
        testing_padded = array(padded)
        predicted_class_label = argmax(
            model.predict(testing_padded),
            axis=-1
        )
        for key, value in emo_code_url.items():
            if value[0]==predicted_class_label:
                predicted_emotion_img_url=value[1]
                predicted_emotion=key
        
        return predicted_emotion, predicted_emotion_img_url