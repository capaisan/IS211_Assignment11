from flask import Flask, redirect, render_template, request

app = Flask(__name__)

todo_list = ['Buy Milk', 'Pay Rent']

@app.route('/')
def show_todo_list():
    name = request.args.get("name", "world")
    todo_item = request.args.get("todo_item")
    return render_template('todo_list.html', name=name)


@app.route('/submit', methods=['POST'])
def submit():
    todo_item = request.form.get("todo_item")
    if not todo_item:
        return "Invalid Entry"
    render_template("success.html")
    # todo_item = request.form['todo_item']
    # todo_list.append(todo_item)
    #
    # return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)
