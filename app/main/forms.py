from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class BlogForm(FlaskForm):

    title = StringField('Blog category',validators=[Required()])
    description = TextAreaField('Write Blog', validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):

    title = StringField('Blog title',validators=[Required()])
    comment = TextAreaField('Blog feedback', validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Add Bio')
