from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<entered>')
def say(entered):
    return f'Hi {entered}!'

@app.route('/repeat/<num>/<entered>')
def repeat(num, entered):
    output = ''
    for i in range(0, int(num)):
        output += entered + '\n'
    return output

if __name__ == "__main__":
    app.run(debug=True)