from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html', x=0, b_color='skyblue')

@app.route('/play')
def play_page():
    return render_template('index.html', x=3, b_color='skyblue')

@app.route('/play/<int:num>')
def custom_play_page(num):
    return render_template('index.html', x=num, b_color='skyblue')

@app.route('/play/<int:num>/<color>')
def color_custom_play_page(num, color='skyblue'):
    return render_template('index.html', x=num, b_color=color)

if __name__ == "__main__":
    app.run(debug=True)