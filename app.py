from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/ImgSend', methods = ['POST', 'GET'])
def ImgSend():
    if request.method == 'POST':
        id = request.form['id']
        print(id)
        return "POST TEST DATA: %s" %id
    elif request.method == 'GET':
        test_json = request.args.get('test')
        print(type(test_json))
        print(test_json)
        return "GET TEST DATA: %s" %test_json

@app.route('/')
def test():
    print('test')
    return '<h1>Hello World<h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5501, debug=True)
