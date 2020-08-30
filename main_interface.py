
import os
from tkinter import * 
from subprocess import Popen
import cv2 
from tkinter import messagebox
from PIL import Image, ImageTk
import numpy as np
import tkinter as tk
import playsound as ps
from tkdocviewer import DocViewer

 
window = Tk()
 
window.title("Security Service using Drones Application")
 
window.geometry('1300x800')
window.configure(background='orange')



width, height = 900, 600
cap = cv2.VideoCapture(0)


lmain =Label(window)
lmain.pack()

def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)

show_frame()

ps.playsound('1.mp3')



#-----------------------------------only lower button  button finctions---------------------------------------------------------



 
def start_sur():
    ps.playsound('9.mp3')
 
    import tkinter as tk
    import cv2
    from PIL import Image, ImageTk
 
    width, height = 800, 600
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
 
    sur = tk.Tk()
    sur.bind(' lambda e: sur.quit()')
    lmain = tk.Label(sur)
    lmain.pack()
 
    def show_frame():
        frame = cap.read()
        frame = cv2.flip(frame, 1)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(10, show_frame)
 
    show_frame()
    sur.mainloop()
    
def stop_sur():
    ps.playsound('3.mp3')
    frame.release 
    
def open_dir():
    ps.playsound('4.mp3')
    os.startfile(r"C:\Users\Lenovo\Desktop\project files") 
    
    
def project_credits():
    ps.playsound('5.mp3')
    messagebox.showinfo('Alert', 'Showing project details')
    
    
    

    
def about_project():
    ps.playsound('6.mp3')
    project_details = Tk()
    v = DocViewer(project_details.txt)
    v.pack(side="top", expand=1, fill="both")
    v.display_file("project details.txt")
    project_details.mainloop()
       
    
    
def get_assistance():
    ps.playsound('1.mp3')
 
#-------------------------------CHATBOT CODE_______________________________________________________________________

    bot = ChatBot(
    'Example Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': .70
        }
    ]
)





    assist_win = Tk()
    assist_win.title("Assistance")
    assist_win.geometry('410x400')
    assist_win.configure(background='Aqua')
    input_msg=" "
    def take_query():
        inputValue=text.get("1.0","end-1c")
        input_msg=inputValue
        response = bot.get_response(input_msg)
        sentence="KDT 1.0--->"+ str(response)
        text1.insert(0.0,sentence)


    def reset_text():
        text.delete('1.0', END)
        text1.delete('1.0', END)
    l1=Label(assist_win,text="Type your query")
    l1.grid(row=0)
    text = Text(assist_win, width=50, height=5, wrap=WORD, selectbackground="blue")
    text.grid(row=2,column=0)
        
        
    btn=Button(assist_win,text="SEND",bg="purple",fg="white",command=take_query)
    btn.grid(row=12,column=0) 
        
        
        
        
    text1 = Text(assist_win, width=50, height=15, wrap=WORD, selectbackground="blue")
    text1.grid(row=13,column=0)
        
    btn=Button(assist_win,text="Reset",bg="purple",fg="white",command=reset_text)
    btn.grid(row=14,column=0) 
        
        
        
        
        

    assist_win.mainloop()
    
#------------------------------------only right button functions-------------------------------------------
    
def comm_police():
    
    def police_comm():
        messagebox.showinfo('Alert', 'Message has been sent to police department')
       
    win=Toplevel()
    win.title("Police communication window")
    win.geometry('310x350')  
    l1=Label(win,text="Name")
    l2=Label(win,text="Purpose")
    l3=Label(win,text="Enter Co-ordinates")
    l4=Label(win,text="Additionl information")
    ent=Entry(win)
    ent2=Entry(win)
    var_chk=IntVar()
    rd1=Radiobutton(win,text='Notice',variable=var_chk,value=1)
    rd2=Radiobutton(win,text='Emergency',variable=var_chk,value=2)
    
    l1.grid(row=0)
    l2.grid(row=1)
    l3.grid(row=3)
    l4.grid(row=4)
    
    
    ent.grid(row=0,column=1)
    rd1.grid(row=1,column=1,sticky=W)
    rd2.grid(row=2,column=1,sticky=W)
    ent2.grid(row=3,column=1)
   
    text = Text(win, width=20, height=10, wrap=WORD, selectbackground="blue")
    text.grid(row=4,column=1)
    
    btn=Button(win,text="SEND",bg="purple",fg="white",command=police_comm)
    btn.grid(row=5,column=1)
    ps.playsound('11.mp3')
    
    
def comm_military():
    ps.playsound('13.mp3')
    def military_comm():
        messagebox.showinfo('Alert', 'Message has been sent to Indian Armed forces')
        
    win=Toplevel()
    win.title("Military communication window")
    win.geometry('310x350')  
    l1=Label(win,text="Name")
    l2=Label(win,text="Purpose")
    l3=Label(win,text="Enter Co-ordinates")
    l4=Label(win,text="Additionl information")
    ent=Entry(win)
    ent2=Entry(win)
    var_chk=IntVar()
    rd1=Radiobutton(win,text='Notice',variable=var_chk,value=1)
    rd2=Radiobutton(win,text='Emergency',variable=var_chk,value=2)
    
    l1.grid(row=0)
    l2.grid(row=1)
    l3.grid(row=3)
    l4.grid(row=4)
    
    
    ent.grid(row=0,column=1)
    rd1.grid(row=1,column=1,sticky=W)
    rd2.grid(row=2,column=1,sticky=W)
    ent2.grid(row=3,column=1)
   
    text = Text(win, width=20, height=10, wrap=WORD, selectbackground="blue")
    text.grid(row=4,column=1)
    
    btn=Button(win,text="SEND",bg="purple",fg="white",command=military_comm)
    btn.grid(row=5,column=1) 
    
    


def comm_fire_brigade():
    ps.playsound('14.mp3')
    def fire_brigade_comm():
        messagebox.showinfo('Alert', 'Message has been sent to Fire brigade')
        
    win=Toplevel()
    win.title("Fire brigade communication window")
    win.geometry('310x350')  
    l1=Label(win,text="Name")
    l2=Label(win,text="Purpose")
    l3=Label(win,text="Enter Co-ordinates")
    l4=Label(win,text="Additionl information")
    ent=Entry(win)
    ent2=Entry(win)
    var_chk=IntVar()
    rd1=Radiobutton(win,text='Notice',variable=var_chk,value=1)
    rd2=Radiobutton(win,text='Emergency',variable=var_chk,value=2)
    
    l1.grid(row=0)
    l2.grid(row=1)
    l3.grid(row=3)
    l4.grid(row=4)
    
    
    ent.grid(row=0,column=1)
    rd1.grid(row=1,column=1,sticky=W)
    rd2.grid(row=2,column=1,sticky=W)
    ent2.grid(row=3,column=1)
   
    text = Text(win, width=20, height=10, wrap=WORD, selectbackground="blue")
    text.grid(row=4,column=1)
    
    btn=Button(win,text="SEND",bg="purple",fg="white",command=fire_brigade_comm)
    btn.grid(row=5,column=1) 

# ----------------------------------Communication system-------------------------------
def broadcast():
    ps.playsound('7.mp3')
    Popen('python broadcast.py')
 
 















def close_application():
    ps.playsound('8.mp3')
 
    window.destroy()
    cap.release()
    
    
    
    
    
 
#------------------------------------------------------all bottom buttons-----------------------------------------------
    
    
    
    
    
    
btn1 = Button(window,text="Start Surveillance Mode", command=start_sur,bg="black",fg="white", width=20, height=4).place(x=10, y=600) 
btn2 = Button(window,text="Stop Surveillance Mode", command=stop_sur,bg="black",fg="white", width=20, height=4).place(x=210, y=600) 

btn3 = Button(window,text="Open Event Directory", command=open_dir,bg="black",fg="white", width=20, height=4).place(x=410, y=600) 


btn4 = Button(window,text="Get Assistance", command=get_assistance,bg="black",fg="white", width=20, height=4).place(x=610, y=600) 

btn5 = Button(window,text="About Project", command=about_project,bg="black",fg="white", width=20, height=4).place(x=810, y=600) 
btn6 = Button(window,text="Project Credits", command=project_credits,bg="black",fg="white", width=20, height=4).place(x=1010, y=600) 


#--------------------------------------all right Buttons--------------------------------------------------------------

btn7 = Button(window,text="Ping Police", command=comm_police,bg="black",fg="white", width=20, height=4).place(x=1140, y=20) 
btn8 = Button(window,text="Ping Military", command=comm_military,bg="black",fg="white", width=20, height=4).place(x=1140, y=140)


btn9 = Button(window,text="Ping Fire Brigade", command=comm_fire_brigade,bg="black",fg="white", width=20, height=4).place(x=1140, y=260)


btn10 = Button(window,text="Broadcast Message", command=broadcast,bg="black",fg="white", width=20, height=4).place(x=1140, y=380)


btn11 = Button(window,text="Close Application", command=close_application,bg="black",fg="white", width=20, height=4).place(x=1140, y=500)




 
window.mainloop()