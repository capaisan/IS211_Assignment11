from flask import Flask, redirect, render_template, request

app = Flask(__name__)

todo_list = {"Name": [], "Email": []}
name_list = []

@app.route('/')
def show_todo_list():

    return render_template('todo_list.html')


@app.route('/submit', methods=['POST'])
def submit():
    todo_item = request.form.get("todo_item")
    email      = request.form.get("email")
    if not todo_item:
        return "Invalid Entry"

    todo_item = request.form['todo_item']
    # email = request.form['email']
    todo_list["Name"].append(todo_item)
    # todo_list["Email"].append(email)


    return redirect("/success")


@app.route('/success', methods=['GET'])
def success():
    return render_template("success.html",
                           todo_list=todo_list)


@app.route('/previous', methods=['GET'])
def previous():
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
