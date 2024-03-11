from wtforms import Form, StringField, IntegerField, FloatField
from wtforms import validators

class EmpleadoForm(Form):
    id = IntegerField('ID', [validators.DataRequired(message="Es necesario obtener el ID")])
    nombre = StringField('Nombre', [validators.DataRequired(message="El nombre es requerido"),
                                   validators.Length(min=5,max=25, message="Ingresa un valor maximo")])
    direccion = StringField('Direccion', [validators.DataRequired(message="La direccion es requerido"),
                                   validators.Length(min=5,max=100, message="Ingresa un valor maximo")])
    telefono = StringField('Telefono', [validators.DataRequired(message="El telefono es requerido"),
                                   validators.Length(min=5,max=100, message="Ingresa un valor maximo")])
    correo = StringField('Correo', [validators.DataRequired(message="El telefono es requerido"),
                                   validators.Length(min=5,max=100, message="Ingresa un valor maximo")])
    sueldo = FloatField('Sueldo', [validators.DataRequired(message="Es necesario agregar el sueldo del empleado")])