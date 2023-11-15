class TodoList:
    def __init__(self):
        self.todo_list = {}

    def add(self, todo):
        self.todo_list[todo.task]=todo.status

    def incomplete(self):
        incomplete = []
        for todo in self.todo_list.items():
            if todo[1] == 'False':
                incomplete.append(todo[0])
        return incomplete
    
    def complete(self):
        complete = []
        for todo in self.todo_list.items():
            if todo[1] == 'True':
                complete.append(todo[0])
        return complete

    def give_up(self):
        # loop through keys and values in dict, update values to true
        for key, value in self.todo_list.items():
            self.todo_list.update({key: "True"})