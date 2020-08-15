from ariadne import QueryType, MutationType
from dev.model.TodoItem import TodoItem
from dev.DAO.helpers import create, delete, fetchAll, setCompleted, updateActivity

query = QueryType()
mutation = MutationType()

@query.field("TodoList")
def resolve_list(_, info):
    return fetchAll()

@mutation.field("createTodo")
def resolve_create(_, info, activity, completed):
    newTodoItem = TodoItem(_id=None, activity=activity, completed=completed)
    create(newTodoItem)
    return fetchAll()

@mutation.field("updateActivity")
def resolve_update(_, info, _id, activity):
    todo = TodoItem(_id, activity, completed=None)
    updateActivity(todo)
    return fetchAll()

@mutation.field("setCompleted")
def resolve_set_completed(_, info, _id, completed):
    todo = TodoItem(_id=_id, completed=completed, activity=None)
    setCompleted(todo)
    return fetchAll()

@mutation.field("deleteTodo")
def resolve_delete(_, info, _id):
    delete(_id)
    return fetchAll()
