from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
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

@app.route('/favorite-course')
def favorite_course():
    subject = request.args.get('subject')
    course_number = request.args.get('course_number')
    return render_template('favorite-course.html',
                           subject=subject,
                           course_number=course_number)

# Contact route that handles both GET and POST requests
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        first_name = (request.form.get('first_name') or '').strip()
        last_name = (request.form.get('last_name') or '').strip()
        email = (request.form.get('email') or '').strip()
        grade = (request.form.get('grade') or '').strip()

        if first_name and last_name and email:
            return render_template('contact.html',
                                   submitted=True,
                                   first_name=first_name,
                                   last_name=last_name,
                                   email=email,
                                   grade=grade)

    return render_template('contact.html', submitted=False)

if __name__ == '__main__':
    app.run()
