from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result')
def result():
    text = request.args.get('text')
    return render_template('result.html', result=len(text))

app.run(debug=True)
