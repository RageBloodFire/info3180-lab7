from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from wtforms.widgets import TextArea
from flask_wtf.file import FileField, FileRequired, FileAllowed

class UploadForm(FlaskForm):
    photo = FileField('Image',validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images Only')])
    description = StringField('Description', validators=[InputRequired()], widget=TextArea())