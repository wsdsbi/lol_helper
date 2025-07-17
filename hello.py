from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

if __name__ == '__main__':
    # debug=True 可以热重载、自动刷新
    app.run(host='0.0.0.0', port=5000, debug=True)