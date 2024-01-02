from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todolist = [
    {"id": 1, "nome": "Estudar programacao"},
    {"id": 2, "nome": "Cozinhar"},
    {"id": 3, "nome": "Lavar a louca"}
]

@app.route('/')
def index():
    return render_template('index.html', todolist=todolist)

@app.route('/adicionar-todo', methods=['POST'])
def adicionar_todo():
    id = len(todolist) + 1
    todo = request.form.get('todo')
    
    todolist.append({"id": id, "nome": todo})

    return redirect(url_for('index'))

@app.route('/remover-todo/<int:id>')
def remover_todo(id):
    for todo in todolist:
        if todo['id'] == id:
            todolist.remove(todo)
            break

    print(todolist)
    return redirect(url_for('index'))