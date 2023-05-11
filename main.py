from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    list1 = ["eat", "drink", "study"]
    return render_template('index.html', list1=list1)


@app.route('/user/<firstname>/<int:age>')
def user(firstname, age):
    return render_template('user.html', firstname=firstname, age=age)


if __name__ == '__main__':
    app.run(debug=True)
