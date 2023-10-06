from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/ImgSend', methods = ['POST', 'GET'])
def ImgSend():
    if request.method == 'POST':
        id = request.form['id']
    print(id)
    return id

@app.route('/')
def test():
    print('test')
    return '<h1>Hello World<h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5501)