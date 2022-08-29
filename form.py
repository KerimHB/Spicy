from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, EmailField
from wtforms.validators import DataRequired, Length, Email


class Datos(FlaskForm):
    nombre = StringField("Nombres", validators=[
        DataRequired(),
        Length(max=30, min=3)
    ])

    apellido = StringField("Apellidos", validators=[
        DataRequired(),
        Length(max=30, min=3)
    ])

    direccion = StringField("Direccion", validators=[
        DataRequired(),
        Length(max=150, min=15)
    ])

    email = EmailField("email", validators=[
        DataRequired(),
        Length(max=30, min=10)
    ])

    mensaje = TextAreaField("Mensaje", validators=[
        DataRequired(),
        Length(max=500, min=4)
    ])

    telefono = StringField("Telefono", validators=[
        DataRequired(),
        Length(max=12, min=8)
    ])


submit = SubmitField("Enviar")
