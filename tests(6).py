import subprocess
from tkinter import *

def run_script():
    # Запустить файл test(5).py в новой вкладке
    subprocess.Popen(["python", "tests(5).py"])

root = Tk()

run_button = Button(root, text="Запустить скрипт", command=run_script)
run_button.pack()

root.mainloop()