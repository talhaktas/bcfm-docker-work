from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/name')
def greet_by_name():
    name = request.args.get('name')
    surname = request.args.get('surname')
    
    if name and surname:
        return f'Hello, {name} {surname}!'
    else:
        return 'Please provide both "name" and "surname" as query parameters.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
