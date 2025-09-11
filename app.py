from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Laith Dasti! This is my first HTML page.'

@app.route('/hello')
def hello():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run()
