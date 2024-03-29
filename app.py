# Todo List with remove
# Written by Mohammad Golmoradizade, m.golmoradi@gmail.com

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = {}

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    #TODO validate input
    content = request.form['content']
    tasks[len(tasks) + 1] = content
    #TODO Return proper notification
    return redirect(url_for('index'))


@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if task_id in tasks:
        del tasks[task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

