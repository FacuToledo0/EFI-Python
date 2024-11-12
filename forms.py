from flask_wtf import FlaskForm
from wtforms import (
    DecimalField,
    IntegerField,
    SelectField,
    StringField,
    SubmitField,
)
from wtforms.validators import (
    DataRequired,
    Length, 

)



class MarcaForm(FlaskForm):
    nombre= StringField(
        'Nombre',
        validators=[Length(min=3, max=40), DataRequired()],
        render_kw={"class":"form-control", "placeholder":"Nombre"}
    )
    submit= SubmitField(
        'Guardar',
        render_kw={"class":"form-control btn btn-success"}
        )
    
class ModeloForm(FlaskForm):
    nombre= StringField(
        'Nombre',
        validators=[Length(min=3, max=40), DataRequired()],
        render_kw={"class":"form-control", "placeholder":"Nombre"}
    )
    submit= SubmitField(
        'Guardar',
        render_kw={"class":"form-control btn btn-success"}
        )


# class TipoForm(FlaskForm):
#     nombre= StringField(
#         'Nombre',
#         validators=[Length(min=3, max=40), DataRequired()],
#         render_kw={"class":"form-control", "placeholder":"Nombre"}
#     )
#     submit= SubmitField(
#         'Agregar',
#         render_kw={"class":"form-control btn btn-success"}
#         )




# class TelefonoCantidadForm(FlaskForm):
#     telefono = SelectField('Teléfono', coerce=int, validators=[DataRequired()])
#     cantidad = IntegerField('Cantidad', validators=[DataRequired()])
#     submit = SubmitField('Guardar')



class EquipoForm(FlaskForm):
    anio_fabricacion = IntegerField('Año de Fabricación', validators=[DataRequired()])
    precio = DecimalField('Precio', validators=[DataRequired()])
    marca = SelectField('Marca', coerce=int)
    modelo = StringField('Modelo', validators=[DataRequired()])
    proveedor = SelectField('Proveedor', coerce=int)
    fabricante = SelectField('Fabricante', coerce=int)
    accesorio = SelectField('Accesorio', coerce=int)
    submit = SubmitField('Agregar')
    

class AccesorioForm(FlaskForm):
    nombre = StringField(
        'Nombre',
        validators=[Length(min=3, max=40), DataRequired()],
        render_kw={"class": "form-control", "placeholder": "Nombre"}
    )
    submit = SubmitField(
        'Agregar',
        render_kw={"class": "form-control btn btn-success"}
    )

class ProveedorForm(FlaskForm):
    # Campo para el nombre del proveedor
    nombre_proveedor = StringField(
        'Nombre del Proveedor',
        validators=[Length(min=3, max=100), DataRequired()],
        render_kw={"class": "form-control", "placeholder": "Nombre del Proveedor"}
    )

    # Campo para el contacto del proveedor (por ejemplo, teléfono o correo)
    contacto = StringField(
        'Contacto',
        validators=[Length(min=3, max=50), DataRequired()],
        render_kw={"class": "form-control", "placeholder": "Contacto"}
    )

    # Botón de envío
    submit = SubmitField(
        'Agregar',
        render_kw={"class": "form-control btn btn-success"}
    )

class FabricanteForm(FlaskForm):
    # Campo para el nombre del proveedor
    nombre_fabricante = StringField(
        'Nombre del Fabricante',
        validators=[Length(min=3, max=100), DataRequired()],
        render_kw={"class": "form-control", "placeholder": "Nombre del Proveedor"}
    )

    # Campo para el contacto del proveedor (por ejemplo, teléfono o correo)
    pais_origen = StringField(
        'País de origen',
        validators=[Length(min=3, max=50), DataRequired()],
        render_kw={"class": "form-control", "placeholder": "Contacto"}
    )

    # Botón de envío
    submit = SubmitField(
        'Agregar',
        render_kw={"class": "form-control btn btn-success"}
    )