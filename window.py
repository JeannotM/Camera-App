from tkinter import messagebox, filedialog
from PIL import ImageTk, Image
from tkinter import *

window = ""
window_bar = ""
window_main = ""

def create_window():
    window = Tk()
    window.title = "Python Camera"
    window.geometry("800x450")

    window_bar = Frame(window)
    window_bar.pack(side=TOP, anchor=NW)
    window_bar.grid(padx=1, pady=1)

    window_main = Frame(window)
    # window_main.pack(side=TOP, anchor=NW)
    window_main.grid(padx=1, pady=1)

    def func():
        messagebox.showinfo("Greetings", "a")

    create_button(window_bar, "Picture", add_picture)
    create_button(window_bar, "Bruh", func)

    window.mainloop()


def create_button(window, innerText, func):
    btn = Button(window, text=innerText, width=8, height=1, command=func)
    btn.pack(side = LEFT, padx=1)


def add_picture():
    photo = filedialog.askopenfile()
    # window.open(photo.name)
    label = Label(window_main, width=20, height=10, bg='green') 
    label.image = photo # keep a reference!
    # label.pack(side = LEFT, padx=1)

    # image = ImageTk.PhotoImage(photo.name)
    # label = Label(window_main, image).pack(side=TOP)
    # messagebox.showinfo("Greetings", photo.name)