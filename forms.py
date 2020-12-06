from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AppendLinkedListForm(FlaskForm):
    data_val = StringField('DataValue', validators=[DataRequired()])
    append = SubmitField('Append')
