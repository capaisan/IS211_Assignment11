from flask import Flask, redirect, render_template, request

app = Flask(__name__)

todo_list = {"Name": [], "Email": [], "Priority": []}


@app.route('/')
def show_todo_list():
    return render_template('todo_list.html')


@app.route('/submit', methods=['POST'])
def submit():
    todo_item = request.form.get("todo_item")
    email = request.form.get("email")
    priority = request.form.get("priority")

    if not todo_item or not email or not priority:
        return "Invalid Entry"

    todo_list["Name"].append(todo_item)
    todo_list["Email"].append(email)
    todo_list["Priority"].append(priority)


    return redirect("/success")


@app.route('/success', methods=['GET'])
def success():
    return render_template("success.html",
                           todo_list=todo_list)


@app.route('/previous', methods=['GET'])
def previous():
    return redirect('/')


@app.route('/clear')
def clear_todo_list():
    global todo_list
    todo_list = {"Name": [], "Email": [], "Priority": []}
    return redirect("/")




if __name__ == '__main__':
    app.run(debug=True)
