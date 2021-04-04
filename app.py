from flask import Flask, render_template, request, redirect, url_for
import pymongo

from User import User

app = Flask(__name__)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        error = None
        name = request.form["name"]
        surname = request.form["surname"]
        email = request.form["email"]
        password = request.form["password"]
        password_val = request.form["password_val"]

        mycollection = mydb["Users"]

        if password == password_val and name != "" and surname != "" and email != "" and len(password) > 8:
            user = User(name, surname, email, password)
            mycollection.insert_one(user.user_json())
            error = "Kayıt olundu."

            return render_template("signin.html", error=error)

    return render_template("register.html")


@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        email = request.form["email_signin"]
        password = request.form["password_signin"]

        mycollection = mydb["Users"]

        result = mycollection.find_one({
            "email": {
                "$eq": email
            }
        })

        if result:
            if result["password"] == password:
                return redirect(url_for("index", name=result["name"]))
    return render_template("signin.html")

@app.route("/index",methods=["GET"])
def index():
    name = request.args.get("name")
    return render_template("index.html", name=name)




if __name__ == "__main__":
    myclient = pymongo.MongoClient(
        "mongodb+srv://frknmydn:frknmydn@cluster0.uxghr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

    mydb = myclient["flaskPrototype"]  # varsa kullanır yoksa oluşturur
    app.run(port=8000, debug=True)
