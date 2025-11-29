FILEPATH = 'todos.txt'

def get_todos(file_path=FILEPATH):
    """
    Reads a text file and returns the list of to-do items.

    :param file_path: The path to the to-do list file (default is "todos.txt").
    :type file_path: str
    :return: A list of to-do items, each ending with a newline character.
    :rtype: list
    """
    with open(file_path, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def store_todos(todos_list, file_path=FILEPATH):
    """
    Writes the list of to-do items to a text file.

    :param todos_list: The list of to-do items (must include '\\n' at the end of each item).
    :type todos_list: list
    :param file_path: The path to the to-do list file (default is "todos.txt").
    :type file_path: str
    :return: None
    """
    with open(file_path, "w") as file_local:
        file_local.writelines(todos_list)


if __name__ == "__main__":
    # test function
    print(get_todos())