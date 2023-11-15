from lib.todo_list import *
from lib.todo import *

def test_incomplete():
    todo = Todo('shopping')
    todo_list = TodoList()
    todo_list.add(todo)
    result = todo_list.incomplete()
    assert result == ['shopping']

def test_complete():
    todo = Todo('shopping')
    todo.mark_complete()
    todo_list = TodoList()
    todo_list.add(todo)
    result = todo_list.complete()
    assert result == ['shopping']

def test_giveup():
    todo1 = Todo('shopping')
    todo2 = Todo('driving')
    todo1.mark_complete()
    todo_list = TodoList()
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.give_up()
    result = todo_list.complete()
    assert result == ['shopping','driving']