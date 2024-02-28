from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, Length, Email

class UserForm(Form):
    ID = IntegerField('ID', validators=[
        validators.DataRequired(message="El ID es requerido"),
        validators.NumberRange(min=1, max=20, message="Valor no válido")
    ])

    nombre = StringField('Nombre', validators=[
        DataRequired(message="El nombre es requerido"),
        Length(min=4, max=50, message="Ingresa un nombre válido (entre 4 y 50 caracteres)")
    ])
    apaterno = StringField("Email", validators=[
        DataRequired(message="El email es requerido"),
        Email(message="Ingresa un email válido")
    ])

    email = IntegerField('Edad', validators=[
        DataRequired(message="La edad es requerida")
    ])