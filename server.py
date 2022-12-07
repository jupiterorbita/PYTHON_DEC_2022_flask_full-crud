from flask import Flask, render_template, request, redirect
from dog_model import Dog
app = Flask(__name__)

#? ---------- READ ALL ------------- 
@app.route("/")
def index():
    all_dogs = Dog.get_all()
    return render_template("dashboard.html", all_dogs=all_dogs)

#? ------------ CREATE VIEW ------------
# /table_name/id/action
@app.route("/dogs/new")
def new_dog_page():
    return render_template("dog_new.html")

#? --------- CREATE ACTION --------------
@app.route("/dogs/create", methods=["post"])
def create_dog():
    print(request.form)
    Dog.create(request.form)
    return redirect("/")

#? ----------- READ ONE -------------
@app.route("/dogs/<int:id>/show")
def show_dog(id):
    data = {
        'id':id
    }
    one_dog = Dog.get_one(data)
    # one_dog = Dog.get_one({'id':id})
    return render_template("dog_show_one.html",one_dog=one_dog)

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")