from flask import Flask
from random import randint

app = Flask(__name__)

random_numb = randint(0, 9)
print(random_numb)


@app.route('/')
def home_page():
    return "<h1>Guess a number between 0 e 9<h1>"\
           "<img src='https://i.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.webp'>"


@app.route('/<int:guess>')
def guess_number(guess):
    if guess > random_numb:
        return "<h1 style='color: purple'>Too low, try again!</h1>"\
               "<img src='https://media.giphy.com/media/tXL4FHPSnVJ0A/giphy.gif'>"

    elif guess < random_numb:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/F77lbfwEAnYNG/giphy.gif'/>"

    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media2.giphy.com/media/1yhHsS7pxo5oI/giphy.gif?cid=ecf05e47b9949zwb0wdw4dz5aylpeh22etjmavov8sp711z0&rid=giphy.gif&ct=g'/>"



if __name__ == "__main__":
    app.run(debug=True)