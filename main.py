from flask import Flask, render_template, request
from flask import flash
#from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
import forms
#from wtforms import validators



from models import db
from models import Alumnos



app = Flask(__name__)

app.config.from_object(DevelopmentConfig)
#csrf = CSRFProtect

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

app.secret_key = "Esta madre se puso buena"

@app.before_request
def before():
    print('before 1')

@app.after_request
def after(response):
    print('after 3')
    return response

@app.route("/")
def index():
    return render_template("layout.html")

@app.route("/alumnos", methods=['GET','POST'])
def alumnos():
    nom = ''
    apa = ''
    ama = ''
    edad = ''

    alumno_clase = forms.UserForm(request.form)
    if request.method == 'POST':
        nom = alumno_clase.nombre.data 
        apa = alumno_clase.apaterno.data 
        ama = alumno_clase.amaterno.data 
        edad = alumno_clase.edad.data 
        print('Nombre: {}'.format(nom))
        print('Apaterno: {}'.format(apa))
        print('Amaterno: {}'.format(ama))

        mensaje = 'Bienvenido {}'.format(nom)
        flash(mensaje)
    return render_template("alumnos2.html", form=alumno_clase, nom = nom, apa = apa, ama = ama)


@app.route('/index', methods=['GET', 'POST'])
def index():
    create_form = forms.UserForm(request.form)
    if request.method == 'POST':
        alum = Alumnos(nombre = create_form.nombre.data,
                       apaterno = create_form.form.data,
                       email = create_form.form.data)
        #insert alumnos() values()
        db.session.add(alum)
        db.session.commit()
    return render_template('index.html', form = create_form)

if __name__ == "__main__":
    #csrf.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()
    app.run()