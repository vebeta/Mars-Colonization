from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class WorkForm(FlaskForm):
    name = StringField('Название работы', validators=[DataRequired()])
    team_leader = StringField('Лидер команды', validators=[DataRequired()])
    duration = StringField('Время на выполнение', validators=[DataRequired()])
    colaborators = StringField('Исполнители', validators=[DataRequired()])
    is_finished = BooleanField('Закончена ли')
    submit = SubmitField('Добавить')
