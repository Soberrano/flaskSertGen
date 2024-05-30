from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

class sertForm(FlaskForm):
  name = StringField('Имя', validators=[DataRequired()])
  sname = StringField('Фамилия', validators=[DataRequired()])
  patronymic = StringField('Отчество', validators=[DataRequired()])
  status = SelectField('Тип сертификата', choices=[('справка', 'справка'), ('сертификат', 'сертификат'), ('сертификат с отличием', 'сертификат с отличием')])
  kvant = StringField('Направление', validators=[DataRequired()])
  mod = SelectField('модуль', choices=[('базовый модуль', 'базовый модуль'), ('угулбленный модуль', 'угулбленный модуль'),('проектный модуль','проектный модуль')])
  hour = StringField('длительность программы', validators=[DataRequired()])
  number = StringField('номер сертификата', validators=[DataRequired()])
  kvantbool = BooleanField('Кванториум')
  cube = BooleanField('IT-Cube')
  submit = SubmitField('Создать')