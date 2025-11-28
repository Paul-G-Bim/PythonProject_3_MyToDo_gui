from functions import get_todos, store_todos
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do", key='todo')
add_button = sg.Button("Add")

layout = [[label],
          [input_box, add_button]]

window = sg.Window("My To-do App", layout=layout)

while True:
    event, value = window.read()
    print(event)
    print(value)
    print(value['todo'])
    match event:
        case 'Add':
            todos = get_todos()
            todos.append(value['todo'] + '\n')
            store_todos(todos)

        case sg.WIN_CLOSED:
            break

window.close()