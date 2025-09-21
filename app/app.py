from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('homepage.html')

@app.route('/post/<year>/<month>/<day>/<post>')
def post(year, month, day, post):
    return render_template(f'{year}/{month}/{day}/{post}.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
