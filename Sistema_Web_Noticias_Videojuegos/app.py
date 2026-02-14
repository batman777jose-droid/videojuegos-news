from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS noticias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            categoria TEXT NOT NULL,
            contenido TEXT NOT NULL,
            fecha TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM noticias ORDER BY fecha DESC")
    noticias = c.fetchall()
    conn.close()
    return render_template('index.html', noticias=noticias)

@app.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        titulo = request.form['titulo']
        categoria = request.form['categoria']
        contenido = request.form['contenido']
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M")

        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO noticias (titulo,categoria,contenido,fecha) VALUES (?,?,?,?)",
                  (titulo,categoria,contenido,fecha))
        conn.commit()
        conn.close()

        return redirect('/')

    return render_template('create.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
