from tkinter import *
from subprocess import Popen
import tkinter as tk






win=Tk()
win.title("Broadcast Window")
win.geometry('330x380')  
win.configure(background='orange')
l1=Label(win,text="Please choose an option")

l2=Label(win,text="NOTE--Please make sure server is onn before starting client")

l1.grid(row=0)
l2.grid(row=1)

def close():
    win.destroy()

def start_server():
    Popen('python server_app.py')

def start_client():
    Popen('python client_app.py')
    
   

btn1 = Button(win,text="Start Server",command=start_server, bg="black",fg="white", width=20, height=4).place(x=90, y=100)     
btn2 = Button(win,text="Start Client",command=start_client, bg="black",fg="white", width=20, height=4).place(x=90, y=180)
btn2 = Button(win,text="Close",command=close, bg="black",fg="white", width=20, height=4).place(x=90, y=290)    
win.mainloop()

#btn=Button(win,text="SEND",bg="purple",fg="white",command=fire_brigade_comm)
#btn1 = Button(window,text="Start Surveillance Mode", command=start_sur,bg="black",fg="white", width=20, height=4).place(x=10, y=600) 
#btn=Button(win,text="SEND",bg="purple",fg="white")
#btn1.grid(row=5,column=1)