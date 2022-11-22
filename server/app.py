from flask import Flask, request

app = Flask(__name__)
database = []

@app.route('/', methods=['GET'])
def home():
    return "5757"


@app.route('/add', methods=['POST'])
def add():
    print(dir(request.data.to_dict()))
    # print(list(request.body.items()))
    return "5757"


if __name__ == '__main__':
    app.run()
