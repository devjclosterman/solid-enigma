# verify if flask is installed correctly
from flask import Flask, render_template

# app = Flask(__name__)
# @app.route('/')
# def hello_world():
#     return 'Hello World!'

# if __name__ == '__main__':
#     app.run(debug=True)

app = Flask(__name__)

#define routes
@app.route('/')
def index():
    return render_template('base.html')

@app.route('/gardening')
def gardening():
    return render_template('gardening.html')

@app.route('/cooking')
def cooking():
    return render_template('cooking.html')

@app.route('/sci-fi')
def sci_fi():
    return render_template('sci_fi.html')

if __name__ == "__main__":
    app.run(debug=True)
