from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@app.route("/register", methods=['GET', 'POST'])
def register():
    return render_template("register.html")

@app.route("/pub", methods=['GET', 'POST'])
def pub():
    return render_template("pub.html")

@app.route("/detail/<int:vegetable_id>")
def detail(vegetable_id):
    return render_template("detail.html")

if __name__ == '__main__':
    app.run()
