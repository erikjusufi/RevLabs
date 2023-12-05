# flask app
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("/index.html")


@app.route("/rest/check_braces", methods=["POST"])
def join_names():
    text = request.get_json()
    missing_braces = {}
    stack = []

    # check for missing closing braces
    for char in text:
        if char == "(" or char == "[" or char == "{":
            stack.append(char)
        elif char == ")":
            if len(stack) == 0 or stack[-1] != "(":
                missing_braces[")"] = missing_braces.get(")", 0) + 1
            else:
                stack.pop()
        elif char == "]":
            if len(stack) == 0 or stack[-1] != "[":
                missing_braces["]"] = missing_braces.get("]", 0) + 1
            else:
                stack.pop()
        elif char == "}":
            if len(stack) == 0 or stack[-1] != "{":
                missing_braces["}"] = missing_braces.get("}", 0) + 1
            else:
                stack.pop()

    # add missing opening braces
    while stack:
        brace = stack.pop()
        missing_braces[brace] = missing_braces.get(brace, 0) + 1

    if missing_braces:
        # return dict with status code 400
        return jsonify(missing_braces), 400
    else:
        # return dict with status code 200
        return jsonify({"message": "All braces are in place"}), 200


if __name__ == "__main__":
    app.run(debug=True)
