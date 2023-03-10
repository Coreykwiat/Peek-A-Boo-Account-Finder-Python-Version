import tkinter as tk
import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import peekaboo
from selenium.common.exceptions import NoSuchElementException

# Define the global variable
username = ""
pin = ""
skip2 = ""
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--silent")
driver = webdriver.Chrome("chromedriver", options=chrome_options)

with open('output.txt', 'r', encoding='utf-8') as file:
    data = file.readlines()

def button_color():
    button.configure(text='Finished', fg='green')

def button_color2():
    button.configure(text='Found You', fg='black')
def titles():
    root.wm_title("Peek-A-Boo is running....")

def titles2():
    root.wm_title("Peek-A-Boo")


def run_script():
    global username
    global pin
    global skip2
    titles()
    username = entry.get()
    pin = pinentry.get()
    skip2 = skipentry.get()
    with open("peekaboo.py", "r") as f:
        script = f.read()
    exec(script)
    button_color()
    titles2()
    webbrowser.open('output.txt')
    time.sleep(2)
    button_color2()



root = tk.Tk()
root.geometry("1280x500")
root.wm_title("Peek-A-Boo")
root.wm_iconbitmap('iseeyou.ico')

frame = tk.Frame(root)
frame.pack(pady=100)


entry_label = tk.Label(frame, text="Enter an email to search for.")
entry_label.pack()
entry = tk.Entry(frame, width=50)
entry.pack()

pin_label = tk.Label(frame, text="Enter a username to try for username based sites (put none for none):")
pin_label.pack()

pinentry = tk.Entry(frame, width=50)
pinentry.pack()

skip_label = tk.Label(frame, text="Skip ones that are known to send reset codes? (put yes for yes to skip)")
skip_label.pack()

skipentry = tk.Entry(frame, width=50)
skipentry.pack()

button = tk.Button(frame,
                   text="Found You",
                   fg="black",
                   command=run_script,)
button.pack(side=tk.RIGHT, padx=150)

image = tk.PhotoImage(file='peekaboo.png')

label = tk.Label(root, image=image)
label.pack(side='top')

disclaimer_label = tk.Label(root, text="DISCLAIMER: THIS TOOL IS FOR LEGAL PURPOSES ONLY AND WHEN THE TOOL IS USED IT WILL ALERT WHOEVER YOU'RE INVESTIGATING AS IT SEND PASSWORD RESET CODES",
                            font=("Arial", 10),
                            anchor=tk.W,
                            justify=tk.LEFT)

disclaimer_label.pack(side=tk.BOTTOM)

root.mainloop()