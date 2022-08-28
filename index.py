from flask import Flask, render_template, request
from form import Datos

app = Flask(__name__)


app.secret_key = '123456'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/panes')
def panes():
    return render_template('panes.html')


@app.route('/complementos')
def complemento():
    return render_template('complementos.html')


@app.route('/bebidas')
def bebida():
    return render_template('bebidas.html')


@app.route('/form', methods=["POST", "GET"])
def Formulario():
    if request.method == "POST":
        return f"nombres= {request.form['nombre']} | apellidos= {request.form['apellido']} | direccion= {request.form['direccion']} |telefono= {request.form['telefono']} | mensaje= {request.form['msg']}"
    return render_template('formulario.html')


@app.route('/contactanos', methods=["POST", "GET"])
def contacto():
    form = Datos()
    if request.method == "POST":
        return f"nombres ={request.form['nombre']} | apellidos={request.form['apellido']} | direccion={request.form['direccion']} | telefono={request.form['telefono']} | Mensaje={request.form['mensaje']}"
    return render_template("contactanos.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
