#   Hellooooo
#   in modularity we trust 
import colors
import image_managment

print(colors.green("__________                     ___________                      "))
print(colors.green("___  ____/_____ ____________  ____  /___(_)__________  _____  __"))
print(colors.green("__  __/  _  __ `/_  ___/_  / / /_  / __  /__  __ \  / / /_  |/_/"))
print(colors.green("_  /___  / /_/ /_(__  )_  /_/ /_  /___  / _  / / / /_/ /__>  < "))
print(colors.green("/_____/  \__,_/ /____/ _\__, / /_____/_/  /_/ /_/\__,_/ /_/|_|"))
print(colors.green("                       /____/                                   "))
print(colors.green("Welcome to EasyLinux!"))
print(colors.green("________________________________________________________________"))

current_file_path = colors.red("?")

def main_menu():
    print(colors.blue("1. Download a Linux Image"))
    print(colors.blue("2. WIP!! Select a Linux Image \t\t\t (" + current_file_path + colors.blue(")")))
    selection = int(input(colors.cyan("Selection: ")))
    
    if selection == 1:
        image_managment.list_downloadables()
    
main_menu()