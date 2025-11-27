from functions import get_todos, store_todos
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do")
add_button = sg.Button("Add")

layout = [[label],
          [input_box, add_button]]

window = sg.Window("My To-do App", layout=layout)
window.read()
window.close()