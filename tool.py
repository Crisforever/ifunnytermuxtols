from colorama import init, Fore
import time
import subprocess

init()

def display_ascii_art(text, color):
    print(color + text)

print(Fore.GREEN)
display_ascii_art("""


    .oooooo.             o8o            .o88o.
   d8P'  `Y8b            `"'            888 `"
  888          oooo d8b oooo   .oooo.o o888oo   .ooooo.  oooo d8b  .ooooo.  oooo    ooo  .ooooo.  oooo d8b
  888          `888""8P `888  d88(  "8  888    d88' `88b `888""8P d88' `88b  `88.  .8'  d88' `88b `888""8P
  888           888      888  `"Y88b.   888    888   888  888     888ooo888   `88..8'   888ooo888  888
  `88b    ooo   888      888  o.  )88b  888    888   888  888     888    .o    `888'    888    .o  888
   `Y8bood8P'  d888b    o888o 8""888P' o888o   `Y8bod8P' d888b    `Y8bod8P'     `8'     `Y8bod8P' d888b
 
""", Fore.GREEN)

print(Fore.MAGENTA + "Github: https://github.com/Crisforever")
time.sleep(2)
print(Fore.BLUE + "Select Tool for download")

print()
print()

print("[1] Keygenerator")
print("[2] isSecureMyPassword")
print()

time.sleep(1)
print(Fore.RED + "Select an option with numbers")

while True:
    try:
        time.sleep(1)
        entrada = input(Fore.MAGENTA + "Enter your option: ")
        option = int(entrada)
        break
    except ValueError:
        time.sleep(1)
        print(Fore.RED + "Please, enter an integer number")


subprocess.run(["bash", "-c", "pkg install git"])
subprocess.run(["bash", "-c", "git init"])
subprocess.run(["bash", "-c", "git remote add origin https://github.com/Crisforever/Python"])
subprocess.run(["bash", "-c", "git config core.sparseCheckout true"])



if option == 1:
    subprocess.run(["bash", "-c", "git sparse-checkout set Keygenerates"])
    subprocess.run(["bash", "-c", "git pull origin main"])
elif option == 2:
    subprocess.run(["bash", "-c", "git sparse-checkout set IsSecureMyPassword"])
    subprocess.run(["bash", "-c", "git pull origin main"])
else:
    print(Fore.RED + "Error: Invalid option or repository does not exist.")
