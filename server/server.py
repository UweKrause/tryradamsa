from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["POST"])
def echo():
    # ToDo: maybe actually do anything with the data to introduce a chance for a failure?
    return request.data


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
