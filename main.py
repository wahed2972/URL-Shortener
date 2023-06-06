from tkinter import *
import pyshorteners

def shorten():
    if short.get():
        short.delete(0,END)
    
    if my_entry.get():
        url = pyshorteners.Shortener().tinyurl.short(my_entry.get())
        
        short.insert(END,url)
        
root = Tk()
root.title("URL Shortener")
root.geometry("500x500")
        
my_label = Label(root,text="Enter Link To Shorten",font=("Helvetica",34))
my_label.pack(pady=20)

my_entry = Entry(root,font=("Helvetica",24))
my_entry.pack(pady=24)

my_button = Button(root,text="Shorten URL",command=shorten,font=("Helvetica",24))
my_button.pack(pady=20)

short_label = Label(root,text="Shortened URL",font=("Helvetica",24))
short_label.pack(pady=50)

short = Entry(root,font=("Helvetica",22),justify=CENTER,width=40,bd=0,bg="systembuttonface")
short.pack(pady=10)


root.mainloop()