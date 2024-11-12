from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from datetime import datetime

app = Flask(__name__)

# Chave que vai cryptografar a senha no DB
app.secret_key = 'your secret key'

# Configuração do MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'SENHA'
app.config['MYSQL_DB'] = 'unlucky'

# Inicialização do MySQL
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dnd')
def dnd():
    return render_template('dnd.html')

@app.route('/ordem')
def ordem():
    return render_template('ordem.html')

@app.route('/cthulhu')
def cthulhu():
    return render_template('cthulhu.html')

@app.route('/loja')
def loja():
    msg = ''
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM commentDB ORDER BY id DESC")
    comment = cursor.fetchall()
    cursor.close()
    return render_template('loja.html', comment=comment, msg=msg)

# Postar Comentário
@app.route('/comment', methods=['GET', 'POST'])
def post_comment():
    # Mensagem de erro
    msg = ''
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM commentDB ORDER BY id DESC")
    comment = cursor.fetchall()
    cursor.close()
    if request.method == 'POST' and 'username' in request.form and 'email' in request.form and 'content' in request.form:
        # Cria variaveis
        username = request.form['username']
        email = request.form['email']
        content = request.form['content']
        now = datetime.now()
        now_date = now.strftime("%d/%m/%Y, %H:%M")

        # Checa se a conta já existe
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM accounts WHERE email = %s', (email,))
        account = cursor.fetchone()
        cursor.close()

        if account:
            # Se a conta ja existe verifica se ela esta certa
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM accounts WHERE username = %s AND email = %s', (username, email,))
            account = cursor.fetchone()
            cursor.close()

            if account:
                # Posta comentário
                cursor = mysql.connection.cursor()
                cursor.execute("INSERT INTO commentDB (username, content, now_date) VALUES (%s, %s, %s)", (username, content, now_date))
                mysql.connection.commit()
                cursor.close()
            else:
                # Mensagem de erro
                msg = 'Email ou username errados!'
                return render_template('loja.html', comment=comment, msg=msg)
        else:
            # Caso não exita conta cria uma e posta o comentário
            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s)', (username, email,))
            mysql.connection.commit()
            cursor.close()

            # Comentário
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO commentDB (username, content, now_date) VALUES (%s, %s, %s)", (username, content, now_date))
            mysql.connection.commit()
            cursor.close()
    return redirect(url_for('loja'))

if __name__ == '__main__':
    app.run(debug=True)
