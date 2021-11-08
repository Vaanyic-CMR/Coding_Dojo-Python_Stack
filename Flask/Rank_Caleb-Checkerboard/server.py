from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', height = 8, width = 8)

@app.route('/4')
def _8x4_():
    return render_template('index.html', height = 4, width = 8)

@app.route('/<int:y>')
def _8xY_(y):
    return render_template('index.html', height = y, width = 8)

@app.route('/<int:y>/<int:x>')
def _XxY_(y, x):
    return render_template('index.html', height = y, width = x)

if __name__ == "__main__":
    app.run(debug=True)