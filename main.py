"""
To-Do List Application (GUI)

Description:
This script implements a simple To-Do List application using the FreeSimpleGUI library.
It allows users to add, edit, and delete tasks, storing the list persistently 
via external functions. It also features a real-time clock and keyboard shortcuts 
for efficient use.
"""
from functions import get_todos, store_todos
import FreeSimpleGUI as sg
import time

# --- GUI Configuration ---
sg.theme('gray gray gray')  # Set the visual theme

# --- Element Definitions ---
clock = sg.Text('', key='clock')  # Element to display the current time
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do", key='todo')  # Input field for user text
add_button = sg.Button("Add")
list_box = sg.Listbox(values=get_todos(),  # Load initial list from file
                      key='todos',
                      enable_events=True,  # Enable events when item is clicked
                      size=(45, 10))
edit_button = sg.Button("Edit")
delete_button = sg.Button('Delete')
exit_button = sg.Button('Exit')

# --- Layout Structure ---
layout = [[clock],
          [label],
          [input_box, add_button],
          [list_box, edit_button, delete_button],
          [exit_button]]

# Create the window and finalize it immediately to allow for pre-loop element binding
window = sg.Window("My To-do App", layout=layout, finalize=True)

# --- Key Binding for Shortcuts ---
# Bind Enter key pressed in the 'todo' input box to a custom event
window['todo'].bind('<Return>', '_ENTER_')
# Bind Delete key pressed in the 'todos' list box to a custom event
window['todos'].bind('<Delete>', '_DELETE_')

# --- Main Event Loop ---
while True:
    # Read events and values every 200ms (timeout allows clock update)
    event, values = window.read(timeout=200)

    # Check for immediate exit conditions (Window X or 'Exit' button)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    # Update the clock element every loop iteration
    window['clock'].update(time.strftime("%b %d, %Y %H:%M:%S"))

    # --- Handle Keyboard Shortcuts (Re-mapping) ---
    if event == 'todo' + '_ENTER_':
        # If an item is selected in the list, remap Enter to 'Edit', otherwise to 'Add'
        event = 'Edit' if values['todos'] else 'Add'

    if event == 'todos' + '_DELETE_':
        # Remap Delete key event to the 'Delete' case
        event = 'Delete'

    # --- Process Events ---
    match event:
        case 'Add':
            todos = get_todos()
            new_todo_text = values['todo'].strip()

            if new_todo_text:
                todos.append(new_todo_text + '\n')  # Add newline for file consistency
                store_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')

        case 'Edit':
            try:
                # Retrieve the selected item (includes \n) and new text
                todo_to_edit_with_newline = values['todos'][0]
                new_todo_text = values['todo'].strip()
                todos = get_todos()

                # Find the index of the exact item string in the list
                index = todos.index(todo_to_edit_with_newline)

                # Replace the old item with the new, ensuring \n is added
                todos[index] = new_todo_text + '\n'

                store_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
                window['todos'].update(set_to_index=[])  # Deselect item
            except IndexError:
                sg.popup("Please select a to-do to edit.")
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
                window['todos'].update(set_to_index=[])  # Deselect item
            except IndexError:
                sg.popup("Please select a to-do to delete.")

        case 'todos':
            # Event triggered when an item in the listbox is clicked
            # Populate the input box with the selected item (without the trailing \n)
            window['todo'].update(value=values['todos'][0].strip())

# --- Cleanup ---
window.close()