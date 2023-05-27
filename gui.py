import os
import tkinter as tk
from tkinter import filedialog
from backup import backup_folder

config_path = "D:/Files/backup_tools/config.txt"

def open_file_dialog():
    file_path = filedialog.askdirectory()
    return file_path

def open_source():
    global source_str
    source_str = open_file_dialog()
    source_label.config(text=source_str)

def open_dest():
    global dest_str
    dest_str = open_file_dialog()
    dest_label.config(text=dest_str)

def open_file():
    with open(config_path, 'r',encoding="utf-8") as file:
        text = file.read()
        text_widget.delete('1.0', tk.END)
        text_widget.insert(tk.END, text)

def add():
    with open(config_path, 'a',encoding="utf-8") as file:
        file.write(source_str+"------"+dest_str+"\n")
    open_file()

def save_file():
    text = text_widget.get('1.0', tk.END)
    with open(config_path, 'w',encoding="utf-8") as file:
        file.write(text)

def backup():
    f = open(config_path,encoding="utf-8")
    lines = f.readlines()
    for line in lines:
        if line.strip()=="":
            continue
        [source,dest] = line.strip().split("------")
        if (not os.path.exists(source)) or (not os.path.exists(dest)):
            print("Error on line : ",line)
            continue
        backup_folder(source,dest)

root = tk.Tk()
root.title("backup")

source_str = ""
source_label = tk.Label(root,text="Empty")
open_button = tk.Button(root, text="Source Folder", command=open_source)
open_button.pack()
source_label.pack()

dest_str = ""
dest_label = tk.Label(root,text="Empty")
dest_button = tk.Button(root, text="Dest Folder", command=open_dest)
dest_button.pack()
dest_label.pack()

add_button = tk.Button(root, text="Add to config file", command=add)
add_button.pack()

save_button = tk.Button(root, text="Save config file", command=save_file)
save_button.pack()

label = tk.Label(root, text="Source folders and destination folders: ")
label.pack(anchor='w')
text_widget = tk.Text(root)
text_widget.pack()
open_file()

backup_button = tk.Button(root,text="Backup",command=backup)
backup_button.pack()

root.mainloop()
