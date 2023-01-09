from flask import Flask, render_template, request, jsonify
from sentiment_analysis import predict

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/getemotion', methods=['POST'])
def review():
    review = request.json.get('data')
    if not review:
        return jsonify({
            'status' : 'error', 
            'message' : 'Empty response'
        })

    emotion, url = predict(review)
    return jsonify({
        'emotion':emotion ,
        'url':url
    })


if __name__  ==  "__main__":
    app.run(debug=True)