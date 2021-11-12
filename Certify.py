from main import *
import tkinter as tk
import time
from tkinter import filedialog
# Function for opening the
# file explorer window

files_dic = {}

def browsecsv(lbl):
    filename = filedialog.askopenfilename(initialdir="\\",
                                          title="Select a File",
                                          filetypes=[('csv files','*.csv')])

    lbl.configure(text="csv file: "+filename)
    files_dic['csv'] = filename


def browsejson(lbl):
    filename = filedialog.askopenfilename(initialdir="\\",
                                          title="Select a File",
                                          filetypes=[('json files','*.json')])

    lbl.configure(text="json file: "+filename)
    files_dic['json'] = filename

# Create the root window
window = tk.Tk()
window.title('Certify v1.7.4')
window.geometry("500x500")
window.config(background="white")

def f1():
    browsecsv(label1)

def f2():
    browsejson(label2)

label1 = tk.Label(text="csv file: no file chosen yet.",width = 100, height = 4,)
button_explore1 = tk.Button(window,text="Choose a csv file",command=f1)

label2 = tk.Label(text="json file: no file chosen yet.",width = 100, height = 4,)
button_explore2 = tk.Button(window,text="Choose a json file",command=f2)

bufferlabel = tk.Label(text="=========================================")

button_explore1.place(relx=0.5,rely=0.1,anchor=tk.CENTER)
label1.place(relx=0.5,rely=0.2,anchor=tk.CENTER)

button_explore2.place(relx=0.5,rely=0.4,anchor=tk.CENTER)
label2.place(relx=0.5,rely=0.5,anchor=tk.CENTER)

bufferlabel.place(relx=0.5, rely=0.3,anchor=tk.CENTER)


def f_main():
    try:
        log = main(files_dic['json'],files_dic['csv'])
        lb=tk.Label(window,text="Certificate creation completed.").place(relx=0.5,rely=0.8,anchor=tk.CENTER)
        tp = tk.Toplevel(window)
        tp.geometry("200x200")
        for i in log:
            tk.Label(tp,text=i).pack()
    except KeyError:
        print(KeyError.with_traceback())
        lb = tk.Label(window, text="Please choose the files first.").place(relx=0.5, rely=0.8, anchor=tk.CENTER)

mainrun = tk.Button(window,text="RUN",command=f_main,width=50).place(relx=0.5,rely=0.7,anchor=tk.CENTER)
# Let the window wait for any events
window.mainloop()


