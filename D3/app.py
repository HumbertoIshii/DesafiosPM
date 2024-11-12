from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/loja')
def loja():
    return render_template('loja.html')

@app.route('/dnd')
def dnd():
    return render_template('dnd.html')

@app.route('/ordem')
def ordem():
    return render_template('ordem.html')

@app.route('/cthulhu')
def cthulhu():
    return render_template('cthulhu.html')

if __name__ == '__main__':
    app.run(debug=True)
