import tkinter as tk
from tkinter import *
import speedtest

def check_speed():
    sp = speedtest.Speedtest()
    sp.get_servers()
    
    down = str(round(sp.download()/(10**6),3))+ " Mbps"
    up = str(round(sp.upload()/(10**6),3))+ " Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)
sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x700")
sp.config(bg="blue")

lab = Label(sp, text="Internet Speed Test", font=("Arial", 30), bg="blue", fg="white")
lab.place(x=40, y=40, width=400, height=50)

lab = Label(sp, text="Download Speed", font=("Arial", 30), bg="blue", fg="white")
lab.place(x=40, y=130, width=400, height=50)

lab_down = Label(sp, text="00", font=("Arial", 30), bg="blue", fg="white")
lab_down.place(x=40, y=200, width=400, height=50)

lab = Label(sp, text="Upload Speed", font=("Arial", 30), bg="blue", fg="white")
lab.place(x=40, y=290, width=400, height=50)

lab_up = Label(sp, text="00", font=("Arial", 30), bg="blue", fg="white")
lab_up.place(x=40, y=360, width=400, height=50)

Button = Button(sp, text="Check Speed", font=("Arial", 20), bg="blue", fg="white", command=check_speed())
Button.place(x=150, y=450, width=200, height=50)
sp.mainloop()