#tkinter module and library
import tkinter as tk
from tkinter import messagebox,filedialog

root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("600x400")

#text area 
text = tk.Text(
    root,                   #root means parent window 
    wrap = tk.WORD,         #wrap the text by words
    font = ("Ariel",12)
)
text.pack(expand=True,fill=tk.BOTH)  #for full view of text

#main logic starts

#when new file opens old one gets deleted
def new_file():
    text.delete(1.0,tk.END)

#open the file
def open_file():
    #open file path dialog
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files","*.txt")]
    )
    if file_path:
        #open file 
        with open(file_path , "r") as file:
            text.delete(1.0,tk.END)
            text.insert(tk.END,file.read())

#save file
def save_file():
    #open save file dialog
    file_path = filedialog.asksaveasfile(
        defaultextension=".txt",
        filetypes=[("Text Files","*.txt")]
    )
    
    if file_path:
        with open(file_path,"w") as file:
            file.write(text.get(1.0,tk.END))
    
    messagebox.showinfo("Info","File saved successfully")

#menu
main_menu = tk.Menu(root)
root.config(menu=main_menu)
file_menu = tk.Menu(main_menu)

#menu should show New , Open , File , Save , Exit
main_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_command(label="Exit",command=root.quit)




#starts and keep the windows open
root.mainloop()


