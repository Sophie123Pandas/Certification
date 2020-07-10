from flask import Flask, render_template
import os

VIZ_FOLDER = os.path.join('static', 'gspng')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = VIZ_FOLDER

@app.route('/')
def home():
    return render_template("hello.html")

@app.route('/gsviz1')
def tconv():
    """Render an HTML template and return"""
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'Taux de conversion par continent.png')
    return render_template("index tconv.html", user_image = full_filename)
    
@app.route('/gsviz2')
def cnxj():
    """Render an HTML template and return"""
    return render_template("index cnxjour.html")

@app.route('/gsviz3')
def traffics():
    """Render an HTML template and return"""
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'Source du traffic.png')
    return render_template("index traffics.html", user_image = full_filename)

@app.route('/gsviz4')
def cnxr():
    """Render an HTML template and return"""
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'Nombre de connections - régions.png')
    return render_template("index region.html", user_image = full_filename)

@app.route('/gsviz5')
def hit():
    """Render an HTML template and return"""
    return render_template("index hitproduit.html")

@app.route('/gsviz6')
def cnxtransacp():
    """Render an HTML template and return"""
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'Connections et transactions par pays.png')
    return render_template("index.html", user_image = full_filename)

if __name__ == '__main__':
   app.run(debug=True)