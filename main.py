from sys import maxsize

from functions import get_todos, store_todos
import FreeSimpleGUI as sg
import time

sg.theme('gray gray gray')

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do", key='todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=get_todos(), key='todos',
                      enable_events=True, size=(45,10))
edit_button = sg.Button("Edit")
delete_button = sg.Button('Delete')
exit_button = sg.Button('Exit')

layout = [[clock],
          [label],
          [input_box, add_button],
          [list_box, edit_button, delete_button],
          [exit_button]]

window = sg.Window("My To-do App", layout=layout)

while True:
    event, values = window.read(timeout=200)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    window['clock'].update(time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case 'Add':
            todos = get_todos()
            todos.append(values['todo'] + '\n')
            store_todos(todos)
            window['todos'].update(values=todos)

        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + '\n'
                store_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select a to-do")

        case 'Delete':
            try:
                todo_to_delete = values['todos'][0]
                todos = get_todos()
                todos.remove(todo_to_delete)
                store_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select a to-do")

        case 'Exit':
            break

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break

window.close()