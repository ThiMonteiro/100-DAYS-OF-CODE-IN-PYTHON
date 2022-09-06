from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph.</p>'\
           '<img src="https://media.giphy.com/media/l0ErLql1cY5YEimwU/giphy.gif">'

@app.route('/bye')
def bye():
    return 'Bye!'

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, your are {number} years old!"


if __name__ == '__main__':
    app.run(debug=True)






