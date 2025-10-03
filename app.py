from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Laith Dasti! This is my first HTML page.'

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about-css')
def about_css():
    return render_template('about-css.html')


@app.route('/greeting')
def greeting():
    return render_template('greeting.html')



if __name__ == '__main__':
    app.run()
