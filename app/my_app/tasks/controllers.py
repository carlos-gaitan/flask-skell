from flask import Blueprint, render_template, request, redirect, url_for

taskRoute = Blueprint('tasks',__name__,url_prefix='/tasks')

tasks_list = ['task1', 'task2', 'task3', 'task4', 'task5']

@taskRoute.route('/')
def index():
    return render_template('dashboard/tasks/index.html', tasks=tasks_list)

@taskRoute.route('/<int:id>')
def show(id:int):
    return 'Show '+str(id)

@taskRoute.route('/delete/<int:id>')
def delete(id:int):
    del tasks_list[id]
    return redirect(url_for('tasks.index'))

@taskRoute.route('/create', methods=['GET', 'POST'])
def create():
    #print(request.form.get('task'))
    #print(request.args.get('task'))
    task = request.form.get('task')
   
    if task is not None :
        tasks_list.append(task)
        #return redirect('/tasks')
        return redirect(url_for('tasks.index'))
    return render_template('dashboard/tasks/create.html')

@taskRoute.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id:int):
    task = request.form.get('task')
    
    if task is not None:
        tasks_list[id] = task
        return redirect(url_for('tasks.index'))
    
    return render_template('dashboard/tasks/update.html')
