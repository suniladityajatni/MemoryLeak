### Flask

from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    l = []
    for i in range(1000):
        l.append(i)
    return {'message': 'Hello World'}

@app.route('/foo')
def foo():
    r = []
    for j in range(1000):
        r.append(j**j)
    return {'message': 'FOO'}

if __name__ == '__main__':
    app.run(port=8000)