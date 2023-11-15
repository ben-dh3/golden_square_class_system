class Todo:
    def __init__(self, task):
        self.task = task
        self.status = 'False'

    def mark_complete(self):
        self.status = 'True'