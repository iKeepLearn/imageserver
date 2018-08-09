from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,SelectField,RadioField,MultipleFileField
from wtforms.validators import DataRequired

class download_form(FlaskForm):
    url = StringField('url',validators=[DataRequired()])
    dir_path = StringField('dir_path',validators=[DataRequired()])
    submit = SubmitField('Download')

class convert_form(FlaskForm):
    lossless = BooleanField('lossless',)
    quality = SelectField('quality')
    dir_path = StringField('dir_path',validators=[DataRequired()])
    submit = SubmitField('Convert To Webp')

class generation_form(FlaskForm):
    dir_path = StringField('dir_path',validators=[DataRequired()])
    submit = SubmitField('Generation')

class rmrepeat_form(FlaskForm):
    url = StringField('url',validators=[DataRequired()])
    dir_path = StringField('dir_path',validators=[DataRequired()])
    submit = SubmitField('Remove Repeat Files')

class split_form(FlaskForm):
    peer = StringField('peer',validators=[DataRequired()])
    dir_path = StringField('dir_path',validators=[DataRequired()])
    submit = SubmitField('split')

class view_form(FlaskForm):
    upimages = MultipleFileField('upimage',validators=[DataRequired()])
    dir_path = StringField('dir_path',validators=[DataRequired()])
    upbutton = SubmitField('Up Image')
    rmbutton = SubmitField('Remove Image')
