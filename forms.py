from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, Length, Email

class UserForm(Form):
    nombre = StringField('Nombre', validators=[
        DataRequired(message="El nombre es requerido"),
        Length(min=4, max=50, message="Ingresa un nombre válido (entre 4 y 50 caracteres)")
    ])
    email = StringField("Email", validators=[
        DataRequired(message="El email es requerido"),
        Email(message="Ingresa un email válido")
    ])
    apaterno = StringField("Apellido Paterno", validators=[
        DataRequired(message="El apellido paterno es requerido"),
        Length(min=4, max=50, message="Ingresa un apellido paterno válido (entre 4 y 50 caracteres)")
    ])
    amaterno = StringField('Apellido Materno', validators=[
        DataRequired(message="El apellido materno es requerido"),
        Length(min=4, max=50, message="Ingresa un apellido materno válido (entre 4 y 50 caracteres)")
    ])
    edad = IntegerField('Edad', validators=[
        DataRequired(message="La edad es requerida")
    ])