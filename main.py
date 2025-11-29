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
            new_todo_text = values['todo'].strip()
            if new_todo_text:
                todos.append(new_todo_text + '\n')
                store_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')

        case 'Edit':
            try:
                todo_to_edit_with_newline = values['todos'][0]
                new_todo_text = values['todo'].strip()
                todos = get_todos()
                index = todos.index(todo_to_edit_with_newline)
                todos[index] = new_todo_text + '\n'
                store_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
                window['todos'].update(set_to_index=[])
            except IndexError:
                sg.popup("Please select a to-do")
            except ValueError:
                sg.popup("Error: Selected item not found in the list for editing. Please try again.")

        case 'Delete':
            try:
                todo_to_delete = values['todos'][0]
                todos = get_todos()
                todos.remove(todo_to_delete)
                store_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
                window['todos'].update(set_to_index=[])
            except IndexError:
                sg.popup("Please select a to-do")

        case 'Exit':
            break

        case 'todos':
            window['todo'].update(value=values['todos'][0].strip())

        case sg.WIN_CLOSED:
            break

window.close()