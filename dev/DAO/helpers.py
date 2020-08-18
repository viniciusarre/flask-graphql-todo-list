try:
    from dev.DAO.Todo import Todo
    from dev.model.TodoItem import TodoItem
except ImportError:
    from dev.DAO import Todo
    from Todo import Todo
    from dev.model import TodoItem
    from TodoItem import TodoItem
    
def fetchAll():
    todoList = []
    for todo in Todo.objects:
        todoList.append(TodoItem(todo._id, todo.activity, todo.completed))
    return todoList

def create(item):
    todo = Todo(activity=item.activity, completed=item.completed)
    todo.save()

def updateActivity(item):
    result = Todo.objects(_id=item._id)
    for todo in result:
        todo.activity = item.activity
        todo.save()

def setCompleted(item):
    result = Todo.objects(_id=item._id)
    for todo in result:
        todo.completed = item.completed
        todo.save()

def delete(id):
    Todo.objects(_id=id).delete()
