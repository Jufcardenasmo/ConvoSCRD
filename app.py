import requests
from flask import Flask, render_template
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'very_secret_key'

bootstrap = Bootstrap(app)


class BudgetForm(FlaskForm):
    name = StringField('Which actor is your favorite?', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = BudgetForm()
    if form.validate_on_submit():
        name = form.name.data
        budget = '30 pesitos'
        return redirect(url_for('result', budget=budget))
    return render_template('index.html', form=form)


@app.route('/result/<budget>', methods=['GET'])
def result(budget):
    return render_template('result.html', budget=budget)


if __name__ == '__main__':
    app.run(debug=True)
