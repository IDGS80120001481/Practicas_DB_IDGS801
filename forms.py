from wtforms import Form, StringField, IntegerField, RadioField, SelectField
from wtforms import validators

class PizzeriaForm(Form):
    id = IntegerField('ID', [validators.DataRequired(message="Es necesario obtener el ID")])
    nombre = StringField('Nombre', [validators.DataRequired(message="El nombre es requerido"),
                                   validators.Length(min=5,max=25, message="Ingresa un valor maximo")])
    direccion = StringField('Direccion', [validators.DataRequired(message="La direccion es requerido"),
                                   validators.Length(min=5,max=100, message="Ingresa un valor maximo")])
    telefono = StringField('Telefono', [validators.DataRequired(message="El telefono es requerido"),
                                   validators.Length(min=5,max=100, message="Ingresa un valor maximo")])
    num_pizzas = IntegerField('Numero Pizzas', [validators.DataRequired(message="Es necesario agregar el numero de pizzas")])
    tam_pizzas = RadioField('Tamaño Pizza', choices=[('Chica', 'Chica $40'), ('Mediana', 'Mediana $80'), ('Grande', 'Grande $120')],
                             validators=[validators.DataRequired(message="Debe seleccionar un tamaño para la pizza")])
    ingredientes = RadioField('Ingredientes', choices=[('Jamon', 'Jamon $10'), ('Piña', 'Piña $10'), ('Champiñones', 'Champiñones $10')],
                             validators=[validators.DataRequired(message="Debe seleccionar un tamaño para la pizza")])
    opciones = [('1', 'Enero'), ('2', 'Febrero'), ('3', 'Marzo'),  ('4', 'Abril'),  ('4', 'Mayo'),  ('6', 'Junio'),  ('7', 'Julio'),  ('8', 'Agosto'),  ('9', 'Septiembre'),
                 ('10', 'Octubre'),  ('11', 'Noviembre'),  ('12', 'Diciembre')]
    fecha = SelectField('Selecciona la opcion de un mes', choices=opciones)