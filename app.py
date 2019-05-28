from flask import Flask,render_template, request
app = Flask(__name__)


@app.route('/')
def mainpage():
    name = request.args.get("name","World!")
    return render_template("index.html",name="Kapali")
@app.route('/pcKapat')
def pcKapat():
    name = request.args.get("name","World!")
    return render_template("index.html",name="Kapali")
@app.route('/pcAc')
def pcAc():
    name = request.args.get("name","World!")
    return render_template("index.html",name="Acik")

if __name__ == '__main__':
    app.run(port=8080)