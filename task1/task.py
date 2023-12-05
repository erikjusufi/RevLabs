# flask app
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("/index.html")


@app.route("/rest/join_names", methods=["POST"])
def join_names():
    names = request.get_json()
    first_names = {id: name for name, id in names["first_names"]}
    last_names = {id: last_name for last_name, id in names["last_names"]}

    # common ids in both lists
    full_names_ids = set(first_names.keys()) & set(last_names.keys())

    full_names = []
    unpaired = []

    # create list of full names
    for id in full_names_ids:
        full_names.append([first_names[id], last_names[id], id])

    # create list of unpaired names
    for id,name in first_names.items():
        if id not in full_names_ids:
            unpaired.append([name,id])
    for id,last_name in last_names.items():
        if id not in full_names_ids:
            unpaired.append([last_name,id])

    # sort full_names by id
    full_names.sort(key=lambda x: x[2])

    return jsonify({"full_names": full_names, "unpaired": unpaired})


if __name__ == "__main__":
    app.run(debug=True)
