from wtforms import SubmitField, BooleanField, StringField, PasswordField, validators, URLField, SelectField
from flask_wtf import FlaskForm

class AddPOST(FlaskForm):

        name = StringField('Name')
        map_url = URLField('map_url')
        img_url = URLField('img_url')
        location = StringField('Location')
        has_sockets = SelectField('Has sockets', choices = [('1', 'Yes'), ('0', 'No')])
        has_toilet = SelectField('Has toilet', choices = [('1', 'Yes'), ('0', 'No')])
        has_wifi = SelectField('Has wifi', choices = [('1', 'Yes'), ('0', 'No')])
        can_take_calls = SelectField('Can u take calls there?', choices = [('1', 'Yes'), ('0', 'No')])
        seats = SelectField('Are there seats?', choices = [('0-10', '0-10'), ('10-20', '10-20'), ('20-30', '20-30'), ('40-50', '40-50'), ('50+', '50+')])
        coffe_price = StringField('Whats the coffee price?')
        submit = SubmitField('Submit')
