import pyfiglet, os

pyfiglet.print_figlet("N O T E S")
print("Exityx thanks you for using this program. \nI hope you enjoy it and leave a review in the developer's telegram: @exityx.")
print("Enter \"help\" for check command list")

notes = {} # Место хранения заметок


def help_com(arg=""):
    if arg == "":
        print(">>>\t\t\t ---==HELP==--- "
              "\n>>> help or help(self) -- Get command list"
              "\n>>> new key -- Create new note"
              "\n>>> open key -- Get the key value"
              "\n>>> del key -- Delete note"
              "\n>>> exit -- Finish program"
              "\n>>> credits -- Find out the project developers"
              "\n>>> clear -- Clear console.")
    elif arg == "new":
        print(">>> This command allows you to create a new note.")
    elif arg == "open":
        print(">>> This command allows you to open an existing note.")
    elif arg == "del":
        print(">>> This command allows you to delete an existing note.")
    elif arg == "exit":
        print(">>> This command completes the execution of the command")
    elif arg == "credits":
        print(">>> This command will let you know who worked on the project.")
    elif arg == "clear":
        print(">>> This command clears the console.")
    elif arg == "list":
        print(">>> This command show all notes.")
    else:
        print(">>> NonValid argument for function \"help\"")

# Функция разпознавания команд
def recognition(entry):
    if entry.startswith("new "):
        name_new_content = entry[4:]
        print(f"New note: \"{name_new_content}\"")
        value_input = input(">>> Value: ")
        notes[name_new_content] = value_input
        # Создание новой заметки

    elif entry.startswith("open "):
        name_open_content = entry[5:]
        if name_open_content in notes:
            print(f">>> {notes[name_open_content]}")
        else:
            print(f">>> Not found note \"{name_open_content}\" for open.")
        # Открытие существующей заметки

    elif entry.startswith("del "):
        name_delete_content = entry[4:]
        if name_delete_content in notes:
            del notes[name_delete_content]
            print(f">>> Note \"{name_delete_content}\" deleted.")
        else:
            print(f">>> Not found note \"{name_delete_content}\" for delete.")
        # Удаление существующей заметки
    elif entry.startswith("help("):
        if entry.endswith(")"):
            help_com(entry[5:-1])
        else:
            print(">>> Invalid format for calling \"help()\" function")
    elif entry.strip() == "help":
        help_com()
        # Вызов функций помощи

    elif entry.strip() == "credits":
        print(">>>\t\t\t   ---==CREDITS==---"
              "\n>>> Participated in the development of: exityx"
              "\n>>> Responsible for setting up the repository and files : exityx")
        # Разработчики
    elif entry.strip() == "exit":
        exit()
        # Выход из программы

    elif entry.strip() == "clear":
        print(">>> We apologize, but this command is not working due to technical problems.")
        # Очищение консоли
    elif entry.strip() == "list":
        for key, value in notes.items():
            print(f">>> {key} -- \"{value}\"")
while True:
    command = input(">>> ")
    recognition(command)
    # Вызов цикла
