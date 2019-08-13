import yaml
from cmd import Cmd

from todo.todo import Task, TodoList

class Prompt(Cmd):
    prompt = '\n$>'
    intro = 'Welcome to todo. For help, type "help" + Enter.'

    def __init__(self):
        super(Prompt, self).__init__()

        with open('database.yaml', 'r') as stream:
            try:
                self.todo_list = yaml.load(stream, Loader=yaml.Loader)
            except yaml.YAMLError as error:
                print(error)
                return
            
    def do_exit(self, inp):
        ''' Save and exit application'''
        with open('database.yaml', 'w') as stream:
            yaml.dump(self.todo_list, stream)
        print("Bye")
        return True

    def do_list(self, inp):
        ''' List all tasks'''
        print(self.todo_list)
        
    def do_add(self, inp):
        ''' Add a new task '''
        title = input("Enter title: ")
        description = input("Enter a description: ")
        self.todo_list.add_task(Task(title=title, description=description))

    def do_delete(self, inp):
        ''' Delete a task '''
        title = input("Enter the title of a task: ")
        self.todo_list.delete_task(title)

    def do_toggle(self, inp):
        ''' Toggle a task between completed and not completed '''
        title = input("Enter the title of a task: ")
        self.todo_list.toggle_task(title)
    
def run():
    # todo_list = TodoList([Task(title='One'), Task(title='Two'),
    #                       Task(title='Three')])
    
    # with open('database.yaml', 'w') as stream:
    #     yaml.dump(todo_list, stream)
    
    Prompt().cmdloop()
