import os

from flask import Flask, render_template, request, send_from_directory
import generate

app = Flask(__name__)
CONTRACT_FOLDER = "static/contract"
app.config['CONTRACT_FOLDER'] = CONTRACT_FOLDER

# this is the main part where the contract will be generated
@app.route("/", methods=["GET", "POST"])
def contract():
    # how do I know which one of the actions was it (Get or Post)?
    if request.method == "GET":
        return render_template("contract.html")
    else: # it must be a post
        # here we generate the contract
        # return f"The data is = {request.form}"
        law = request.form['lawyer']
        client = request.form['client']
        service = request.form['service']
        comp = request.form['comp']
        deposit = request.form['deposit']
        deposit_date = request.form['deposit_date']
        jur = request.form['jur']
        for f in os.listdir(app.config['CONTRACT_FOLDER']):
            os.remove(os.path.join(app.config['CONTRACT_FOLDER'], f))
        filename = generate.generate(app, law, client, service, comp, deposit, deposit_date, jur)
        return send_from_directory(app.config['CONTRACT_FOLDER'], filename, as_attachment=True)


@app.route("/<name>")
def hello_name(name):
    return render_template("greeting.html", name_of_person=name)


@app.route("/mountains")
def show_template():
    return render_template("mountains.html")

if __name__ == "__main__":
    app.run(debug=True)
