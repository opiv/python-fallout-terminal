
# REQUIRED LIBS
import os;from pynput import keyboard

# OPTIONAL LIBS
import webbrowser,sys;from colorama import init,Fore,Back;init()

words = ["OPTION 1","OPTION 2","GITHUB","EXIT"] # Add your options here
sel = 0

def update_menu(key):
    global sel
    try:
        if key == keyboard.Key.up and sel > 0:
            sel -= 1
        elif key == keyboard.Key.down and sel < len(words) - 1:
            sel += 1
        elif key == keyboard.Key.enter or key == keyboard.Key.space:
            guess = words[sel]
            input("") #required to prevent the "enter" from skipping your next input
            os.system("cls || clear")
            if guess=="OPTION 1":
                #   put your function here :)
                print("option 1 pressed :)")
                os.system("pause")
                sys.exit()
            elif guess=="OPTION 2":
                #   put your other function here :)
                print("opton 2 pressed :)")
                os.system("pause")
                sys.exit()
            elif guess=="GITHUB":
                #   put your other function here :)
                webbrowser.open("https://github.com/opiv")
                sys.exit()
            elif guess=="EXIT":
                sys.exit()
            else:
                print("something went wrong :/")
        print_menu()
    except AttributeError:
        pass
def print_menu():
    global sel
    print("\033c", end="")
    print(f"{Fore.GREEN}Fallout Terminal\nVisit my github: github.com/opiv\n===============================================\nSelect via arrow keys and enter.\n\n")
    for idx, word in enumerate(words):
        if idx == sel:
            print(f"{Back.GREEN}{Fore.BLACK}> {word}{Fore.RESET}{Back.RESET}")
        else:
            print(f"{Fore.GREEN}  {word}")
print_menu()
with keyboard.Listener(on_press=update_menu) as listener:
    listener.join()
