from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello World !!'

@app.route('/super_simple')
def super_simple():
    return jsonify(message='Welcome to super simple Galaxy !')


@app.route('/not_found')
def not_found():
    return jsonify(message='Not Found'), 404


@app.route('/parameters')
def parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    if age < 18:
        return jsonify(message='Sorry, ' + name + ' Not allowed to enter site ')  
    else:
        return jsonify(message='Welcome, ' + name + ' you are allowed to enter !')

@app.route('/url_variables/<string:name>/<int:age>')
def url_variables(name: str, age: int):
  if age < 18:
    return jsonify(message='Sorry, ' + name + ' Not allowed to enter site ')  
  else:
    return jsonify(message='Welcome, ' + name + ' you are allowed to enter !')


if __name__ == "__main__":
    app.run()