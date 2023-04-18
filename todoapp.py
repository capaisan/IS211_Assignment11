from flask import Flask, redirect, render_template, request

app = Flask(__name__)

todo_list = ['Buy Milk', 'Pay Rent']

@app.route('/')
def show_todo_list():
    return render_template('todo_list.html')


@app.route('/submit', methods=['POST'])
def submit():
    todo_item = request.form['todo_item']
    todo_list.append(todo_item)

    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)
