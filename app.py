from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/noticias')
def noticias():
    return render_template('noticias.html')

@app.route('/categorias')
def categorias():
    return render_template('categorias.html')

# Area de juegos

@app.route('/minecraft')
def minecraft():
    return render_template('minecraft.html')

@app.route('/hollow_knight')
def hollow_knight():
    return render_template('hollow_knight.html')

@app.route('/the_legend_zelda')
def the_legend_zelda():
    return render_template('the_legend_zelda.html')

@app.route('/fifa08')
def fifa08():
    return render_template('fifa08.html')

@app.route('/cod_blackops')
def cod_blackops():
    return render_template('cod_blackops.html')

@app.route('/gta_3')
def gta_3():
    return render_template('gta_3.html')

@app.route('/geometry_dash')
def geometry_dash():
    return render_template('geometry_dash.html')

@app.route('/roblox')
def roblox():
    return render_template('roblox.html')

@app.route('/elder_ring')
def elder_ring():
    return render_template('elder_ring.html')

@app.route('/animal_crossing')
def animal_crossing():
    return render_template('animal_crossing.html')

@app.route('/red_dead_redeption_2')
def red_dead_redeption_2():
    return render_template('red_dead_redeption_2.html')

@app.route('/unpacking')
def unpacking():
    return render_template('unpacking.html')

@app.route('/the_witcher_3')
def the_witcher_3():
    return render_template('the_witcher_3.html')

@app.route('/cuphead')
def cuphead():
    return render_template('cuphead.html')

@app.route('/fall_guys')
def fall_guys():
    return render_template('fall_guys.html')

@app.route('/among_us')
def among_us():
    return render_template('among_us.html')

# Area de Noticias

@app.route('/noticia_1')
def noticia_1():
    return render_template('noticia_1.html')

@app.route('/noticia_2')
def noticia_2():
    return render_template('noticia_2.html')
    
@app.route('/noticia_3')
def noticia_3():
    return render_template('noticia_3.html')

@app.route('/noticia_4')
def noticia_4():
    return render_template('noticia_4.html')

@app.route('/noticia_5')
def noticia_5():
    return render_template('noticia_5.html')

@app.route('/noticia_6')
def noticia_6():
    return render_template('noticia_6.html')

if __name__ == '__main__':
    app.run(debug=True)