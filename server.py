from flask import Flask, render_template, request, redirect
# import the class from friend.py
from user import User
app = Flask(__name__)


@app.route("/")
def index():
    # call the get all classmethod to get all friends
    users = User.get_all()
    print(users)
    return render_template("index.html", all_users=users)
            
@app.route("/new_user")
def new_user():
    return render_template("create.html")
    
@app.route("/create_user", methods=["POST"])
def create_user():
    data = {
        "fname" : request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)