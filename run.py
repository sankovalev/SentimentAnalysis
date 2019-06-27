__author__ = 'Alexander Kovalev'
from sentiment_classifier import SentimentClassifier
from codecs import open
from flask import Flask, render_template, request

app = Flask(__name__)

classifier = SentimentClassifier()

@app.route("/SA", methods=["POST", "GET"])
def index_page(text="", prediction_message="", footer_color='#5CAED6'):
    if request.method == "POST":
        text = request.form["review"]
        prediction_message, footer_color = classifier.get_prediction_message(text)
        with open("SA_logs.txt", "a", "utf-8") as log:
            log.write("<response> {0} : {1} /response>".format(text, prediction_message))

    return render_template('SA.html', text=text, prediction_message=prediction_message, footer_color=footer_color)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
