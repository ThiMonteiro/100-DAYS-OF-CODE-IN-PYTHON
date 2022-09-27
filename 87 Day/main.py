from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request
from flask import redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL


app = Flask(__name__)
app.config['SECRET_KEY'] = ""
Bootstrap(app)
file_csv = ""


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


class CafeForm(FlaskForm):
    name = StringField('Cafe name', validators=[DataRequired()])
    map_url = StringField(
        'Cafe Location on Google Maps (URL)',
        validators=[DataRequired(), URL()])
    img_url = StringField(
        'Image (URL)',
        validators=[DataRequired(), URL()])
    location = StringField('Location', validators=[DataRequired()])
    has_sockets = SelectField(
        'Has Sockets?', validators=[DataRequired()], choices=[
            ("0", "❌"),
            ("1", "✅"),

        ], validate_choice=True)
    has_toilet = SelectField(
        'Has Toilets?', validators=[DataRequired()], choices=[
            ("0", "❌"),
            ("1", "✅"),

        ], validate_choice=True)
    has_wifi = SelectField(
        'Has Wifi?', validators=[DataRequired()], choices=[
            ("0", "❌"),
            ("1", "✅"),

        ], validate_choice=True)

    can_take_calls = SelectField(
        'Can Take Calls?', validators=[DataRequired()], choices=[
            ("0", "❌"),
            ("1", "✅"),
        ], validate_choice=True)

    seats = SelectField(
        'Seats', validators=[DataRequired()], choices=[
            ("0-10", "0-10"),
            ("20-30", "20-30"),
            ("30-40", "30-40"),
            ("50+", "50+"),
        ], validate_choice=True)

    coffee_price = StringField('Coffee Price', validators=[DataRequired()])

    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True\n\n")

        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("location"),
            has_sockets=bool(request.form.get("has_sockets")),
            has_toilet=bool(request.form.get("has_toilet")),
            has_wifi=bool(request.form.get("has_wifi")),
            can_take_calls=bool(request.form.get("can_take_calls")),
            seats=request.form.get("seats"),
            coffee_price=request.form.get("coffee_price"),
        )
        db.session.add(new_cafe)
        db.session.commit()

        return redirect(url_for('get_all_cafes'))

    return render_template('add.html', form=form)


@app.route("/cafes")
def get_all_cafes():
    cafes = db.session.query(Cafe).all()
    list_of_rows = []
    for cafe in cafes:
        list_of_rows.append(cafe)

    return render_template('cafes.html', cafes=list_of_rows)


@app.route("/report-closed/<int:cafe_id>")
def delete_cafe(cafe_id):
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        db.session.delete(cafe)
        db.session.commit()

    return redirect(url_for('get_all_cafes'))


if __name__ == '__main__':
    app.run(debug=True)