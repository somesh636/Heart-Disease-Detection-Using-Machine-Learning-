from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators 

app = Flask(__name__,
            static_url_path = "",
            static_folder = "/static" ,
            template_folder = "/templates")

class HelloForm(Form):
    sayhello = TextAreaField('', [validators.DataRequired()])

@app.route('/')
def index():
    form = HelloForm(request.form)
    return render_template('index.htm', form = form)

@app.route('/hello', methods=['POST'])
def hello():
    form = HelloForm(request.form)
    if request.method == 'POST' and form.validate():
        name = request.form['sayhello']
        return render_template('hello.html', name = name)
    return render_template('index.htm', form = form)

if __name__ == '__main__':
    app.run(debug=True)
