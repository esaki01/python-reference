from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello world!'


@app.route('/hello/<username>', methods=['GET'])
def hello_world(username=None):
    if request.method == 'GET':
        # return 'hello world! {}'.format(username)
        return render_template('hello.html', username=username)


if __name__ == '__main__':
    app.run(debug=True)
