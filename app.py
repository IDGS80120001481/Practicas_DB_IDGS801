from flask import Flask, redirect, render_template, request, url_for, Response
import forms
from Pizza import Pizza
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect

from models import db
from models import Pizzeria, Empleado
import EmpleadosForms

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

pizzas = []

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404
 
@app.before_request
def before_request():
    print("before 1")
   
@app.after_request
def after_request(response):
    print("after 3")
    return response

@app.route("/", methods=["GET","POST"])
def add_list(): 
    form = forms.PizzeriaForm(request.form)
    if request.method=="POST":
        
        subtotal = 0
        if form.tam_pizzas.data == 'Chica':
            subtotal = (form.num_pizzas.data * 40) + (form.num_pizzas.data * 10)
        elif form.tam_pizzas.data == 'Mediana':
            subtotal = (form.num_pizzas.data * 80) + (form.num_pizzas.data * 10)
        elif form.tam_pizzas.data == 'Grande':
            subtotal = (form.num_pizzas.data * 120) + (form.num_pizzas.data * 10)
        else:
            subtotal = 0

        pizza_add = Pizza(len(pizzas),
                          form.nombre.data, 
                          form.direccion.data, 
                          form.telefono.data, 
                          form.num_pizzas.data, 
                          form.tam_pizzas.data, 
                          form.ingredientes.data, 
                          subtotal)
        pizzas.append(pizza_add)
    return render_template("index.html",form= form, pizzas = pizzas)

@app.route("/remove", methods=["GET","POST"])
def remove():
    return render_template("remove.html",pizzas=pizzas)

@app.route("/remove_list", methods=["GET","POST"])
def remove_list():

    form = forms.PizzeriaForm(request.form)
    if request.method=="GET":
        index = request.args.get("index")
        print(index)
        pizzas.pop(int(index))
    return render_template("index.html",form = form, pizzas=pizzas)

@app.route("/total", methods=["GET","POST"])
def total():
    total = 0

    for pizza in pizzas:
        total += pizza.subtotal
    return render_template("total.html",total=total)

@app.route("/finish", methods=["GET","POST"])
def finish():
    form=forms.PizzeriaForm(request.form)
    if request.method=="GET":
        for pizza in pizzas:
            pizzeria = Pizzeria(nombre =pizza.nombre,
                direccion = pizza.direccion,
                telefono = pizza.telefono,
                num_pizzas = pizza.num_pizzas,
                tam_pizzas = pizza.tam_pizzas,
                ingredientes = pizza.ingredientes)
            db.session.add(pizzeria)
            db.session.commit()
        pizzas.clear()
    return render_template("index.html", form= form)

@app.route("/update_list", methods=["GET","POST"])
def update_list():
    return render_template("update_list.html",pizzas=pizzas)

@app.route("/update_page", methods=["GET","POST"])
def update_page():
    form = forms.PizzeriaForm(request.form)
    if request.method=="GET":
            index = request.args.get("index")
            pizza = pizzas[int(index)]
            form.id.data= index
            form.nombre.data= pizza.nombre
            form.direccion.data= pizza.direccion
            form.telefono.data= pizza.telefono
            form.num_pizzas.data = pizza.num_pizzas
            form.tam_pizzas.data = pizza.tam_pizzas
            form.ingredientes.data = pizza.ingredientes
        
    return render_template("update.html", form = form, pizzas=pizzas, index = index)


@app.route("/update", methods=["GET","POST"])
def update():
    
    form = forms.PizzeriaForm(request.form)
    if request.method=="POST":
        
        subtotal = 0
        if form.tam_pizzas.data == 'Chica':
            subtotal = (form.num_pizzas.data * 40) + (form.num_pizzas.data * 10)
        elif form.tam_pizzas.data == 'Mediana':
            subtotal = (form.num_pizzas.data * 80) + (form.num_pizzas.data * 10)
        elif form.tam_pizzas.data == 'Grande':
            subtotal = (form.num_pizzas.data * 120) + (form.num_pizzas.data * 10)
        else:
            subtotal = 0

        pizza_add = Pizza(form.id.data,
                          form.nombre.data, 
                          form.direccion.data, 
                          form.telefono.data, 
                          form.num_pizzas.data, 
                          form.tam_pizzas.data, 
                          form.ingredientes.data, 
                          subtotal)
        
        pizzas[int(form.id.data)] = pizza_add
        print(pizzas[int(form.id.data)])
    return render_template("update_list.html",form = form, pizzas = pizzas)

@app.route("/list", methods=["GET","POST"])
def list():
    form = forms.PizzeriaForm(request.form)
    return render_template("pizzas_list.html", form = form)


@app.route("/search", methods=["GET","POST"])
def search():
    form = forms.PizzeriaForm(request.form)
    if request.method=="POST":
        search = form.fecha.data
        print(search)
        pizzas = Pizzeria.query.filter(db.extract('month', Pizzeria.create_date) == search).all()

    return render_template("pizzas_list.html", form = form, pizzas = pizzas)


''' Archivos para el crud de empleados '''

@app.route("/add", methods=["GET","POST"])
def add():
    form = EmpleadosForms.EmpleadoForm(request.form)
    if request.method=="POST":
        emp = Empleado(nombre = form.nombre.data,
                        direccion = form.direccion.data,
                        telefono= form.telefono.data,
                        correo= form.correo.data,
                        sueldo= form.sueldo.data)
        db.session.add(emp)
        db.session.commit()
    return render_template("empleados.html",form=form)

@app.route("/delete_emp",methods=["GET","POST"])
def empleados_manage():
    form= EmpleadosForms.EmpleadoForm(request.form)
    if request.method=="GET":
        id = request.args.get("id")
        emp = db.session.query(Empleado).filter(Empleado.id==id).first()
        form.id.data = request.args.get("id")
        form.nombre.data = emp.nombre
        form.direccion.data = emp.direccion
        form.telefono.data = emp.telefono
        form.correo.data = emp.correo
        form.sueldo.data = emp.sueldo
        
    if request.method=="POST":
        id = form.id.data
        emp = db.session.query(Empleado).filter(Empleado.id==id).first()
        emp.nombre= form.nombre.data
        emp.direccion= form.direccion.data
        emp.telefono= form.telefono.data
        emp.correo= form.correo.data
        emp.sueldo= form.sueldo.data
        db.session.delete(emp)
        db.session.commit()
        return redirect(url_for('manage'))
    return render_template("empleados_delete.html",form = form)

@app.route("/update_emp",methods=["GET","POST"])
def update_emp():
    form = EmpleadosForms.EmpleadoForm(request.form)
    if request.method=="GET":
        id = request.args.get("id")
        emp = db.session.query(Empleado).filter(Empleado.id==id).first()
        form.id.data = request.args.get("id")
        form.nombre.data = emp.nombre
        form.direccion.data = emp.direccion
        form.telefono.data = emp.telefono
        form.correo.data = emp.correo
        form.sueldo.data = emp.sueldo
    if request.method == "POST":
        id = form.id.data
        emp = db.session.query(Empleado).filter(Empleado.id==id).first()
        emp.nombre= form.nombre.data
        emp.direccion= form.direccion.data
        emp.telefono= form.telefono.data
        emp.correo= form.correo.data
        emp.sueldo= form.sueldo.data
        db.session.add(emp)
        db.session.commit()
        return redirect(url_for('manage'))
    return render_template("empleados_update.html",form = form)

@app.route("/manage", methods=["GET","POST"])
def manage():
    form = EmpleadosForms.EmpleadoForm(request.form)
    empleados = Empleado.query.all()

    return render_template("empleados_manage.html",form = form,empleados = empleados)

if __name__=="__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=5000)