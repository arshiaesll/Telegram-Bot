import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    # serve the public/index.html file
    return flask.send_from_directory('public', 'index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
