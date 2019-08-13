import yaml
import datetime

class Task(yaml.YAMLObject):
    yaml_tag = '!task'
    
    def __init__(self, title='Title',
                 description='Description', completed=False):
        self.title = title
        self.date = datetime.date.today()
        self.description = description
        self.completed = completed

    def __str__(self):
        if self.completed:
            box = '[X] '
        else:
            box = '[ ] '
        s = (box
             + f'Title: {self.title}\n'
             + f'Date: {self.date}\n'
             + f'Description: {self.description}\n')
        return s
        
class TodoList(yaml.YAMLObject):
    yaml_tag = '!todo_list'

    def __init__(self, tasks = []):
        self.tasks = tasks

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                return
        print('Task not found.')

    def toggle_task(self, title):
        for task in self.tasks:
            if task.title == title:
               task.completed = not task.completed
               return
        print('Task not found.')
        
    def __str__(self):
        s = "\n"
        for task in self.tasks:
            if task.completed:
                s += f'\n{task}\n'
        for task in self.tasks:
            if not task.completed:
                s += f'\n{task}\n'
        return s
