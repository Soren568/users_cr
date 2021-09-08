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
    User.save(request.form)
    return redirect('/')

@app.route("/users/<int:id>")
def user_view(id):
    data = {
        "id": id
    }
    return render_template("user_info.html", user=User.get_one(data))
    
@app.route('/user/update', methods=["POST"])
def update():
    User.update(request.form)
    return redirect('/')

@app.route("/users/<int:id>/edit")
def edit(id):
    data = {
        "id":id
    }
    return render_template("edit_user.html", user=User.get_one(data))

@app.route("/delete/<int:id>")
def delete_user():
    data = {
        "id" : id
    }
    User.delete_one(data)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)