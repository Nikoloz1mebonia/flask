from flask import Flask, request, redirect, session, url_for, render_template

app = Flask(__name__)
app.secret_key = 'Python'


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/user")
def user():
    if 'username' in session and len(session['username']) > 0:
        user = session['username']
        return render_template('user.html', user=user)
    else:
        return redirect(url_for('login'))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        session['username'] = request.form["username"]
        return redirect(url_for('user'))

    return render_template('login.html')


@app.route("/logout")
def logout():
    session.pop("username", None)
    return render_template('logout.html')


if __name__ == '__main__':
    app.run(debug=True)
