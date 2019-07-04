from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):

    title = StringField('Pitch title',validators=[Required()])
    description = TextAreaField('Pitch feedback', validators=[Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):

    title = StringField('Pitch title',validators=[Required()])
    comment = TextAreaField('Pitch feedback', validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
