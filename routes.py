from flask import Flask, render_template
from forms import RegisterForm

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/register')
def register_page():
    form = RegisterForm()
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
