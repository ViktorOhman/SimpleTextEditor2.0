#Code by github.com/ViktorOhman
import tkinter as tk
import os
import keyboard
import pyautogui

window = tk.Tk()
window.geometry("1920x1080")
window.title("TextEditor2!")
#Create a function for saving files
def save_file(is_saved=True): 
    text_box_contense = text_box.get("1.0", tk.END)
    if is_saved==False:
        file_name = pyautogui.prompt(text="What sholud the name of the file be?")
        is_saved = True
        with open(file_name+".txt","w") as file:
            file.write(text_box_contense)
            lastFileRegistry_wirite(file_name)
    else:
        fileList = []
        for file in os.listdir():
            fileList.append(file)
            if file == "lastFileRY.key":
                with open("lastFileRY.key","r") as lastF:
                    file_to_save_to = lastF.read()
                with open(file_to_save_to,"w") as file:
                    file.write(text_box_contense)
#Create a control function for saving new files
def save_new_file():
    save_file(is_saved=False)
    save_button.pack()
#Create a function for writing to the last file registry
def lastFileRegistry_wirite(lastFileName):
    with open("lastFileRY.key","w") as lastF:
        lastF.write(lastFileName+".txt")
#Create a function for opening a file
def open_file():
    fileName = pyautogui.prompt(text="What is the name(if the file is in this directory) or Path of your file?\nDon't type .txt after the file")
    with open(fileName+".txt","r") as file:
        opend_file_text = file.read()
    text_box.delete("1.0", tk.END)
    text_box.insert("1.0",opend_file_text)
    lastFileRegistry_wirite(fileName)
    save_button.pack()
#Create functions for buttons
def clear():
    text_box.delete("1.0", tk.END)
def copy():
    keyboard.send("ctrl+c")
def cut():
    keyboard.send("ctrl+x")
def paste():
    keyboard.send("ctrl+v")
#Create the text area
text_box = tk.Text(width=180,height=55)
text_box.pack(side=tk.RIGHT)
#Button for clearing
clear_button = tk.Button(text="Clear",width=15,height=3,bg="black",fg="white",command=clear)
clear_button.pack()
#Button for copying
copy_button = tk.Button(text="Copy",width=15,height=3,bg="black",fg="white",command=copy)
copy_button.pack()
#Button for cuting
cut_button = tk.Button(text="Cut",width=15,height=3,bg="black",fg="white",command=cut)
cut_button.pack()
#Button for pasting
paste_button = tk.Button(text="Paste",width=15,height=3,bg="black",fg="white",command=paste)
paste_button.pack()
#Button for saving
save_button = tk.Button(text="Save",width=15,height=3,bg="black",fg="white",command=save_file)
#Button for opening
open_button = tk.Button(text="Open",width=15,height=3,bg="black",fg="white",command=open_file)
open_button.pack()
#Button for saving a new file
save_new_button = tk.Button(text="Save New",width=15,height=3,bg="black",fg="white",command=save_new_file)
save_new_button.pack()

tk.mainloop()#The main loop :D