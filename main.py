from functions import get_todos, store_todos
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do", key='todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=get_todos(),
                      key='todos',
                      enable_events=True,
                      size=(45,10))
edit_button = sg.Button("Edit")

layout = [[label],
          [input_box, add_button],
          [list_box, edit_button]]

window = sg.Window("My To-do App", layout=layout)

while True:
    event, values = window.read()
    print(event)
    print(values)
    # print(value['todo'])
    # print(value['todos'])
    match event:
        case 'Add':
            todos = get_todos()
            todos.append(values['todo'] + '\n')
            store_todos(todos)
            window['todos'].update(values=todos)

        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + '\n'
            store_todos(todos)
            window['todos'].update(values=todos)

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break

window.close()