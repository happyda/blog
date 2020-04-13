from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, BooleanField
from wtforms.validators import DataRequired,Email,EqualTo, Length


class RegisterForm(FlaskForm):
    
    realname = StringField('Realname',validators=[DataRequired()])
    username = StringField('Username',validators=[DataRequired(),Length(min=3,max=16)])
    email = StringField('email',validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    comfirm_pwd = PasswordField('Comfirm Pass', validators=[DataRequired(),EqualTo(password)])
    submit = SubmitField('')

class LoginForm(FlaskForm):
    
    email = StringField('email',validators=[DataRequired(),Email(message='電子郵件格式錯誤')])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember')
    submit = SubmitField('Login')

    

