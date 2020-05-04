from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class UploadForm(FlaskForm):
    photo = FileField('Image',validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images Only')])
    description = TextAreaField('Description', validators=[InputRequired()])