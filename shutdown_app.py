from tkinter import*
import os

def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 10")
def log_out():
    os.system("shutdown -l")      
def shutdown():
    os.system("shutdown /s /t 1")      

st = Tk()
st.title("Shutdown Application")
st.geometry("500x500")
st.config(bg="lightblue")

r_button= Button(st, text="Restart", bg="black", fg="white", command=restart)
r_button.place(x=100, y=200, width=100, height=50)
rt_button= Button(st, text="Restart time", bg="black", fg="white", command=restart_time)
rt_button.place(x=300, y=200, width=100, height=50)
lg_button= Button(st, text="Log-Out", bg="black", fg="white", command=log_out)
lg_button.place(x=200, y=100, width=100, height=50)
st_button= Button(st, text="Shutdown", bg="black", fg="white", command=shutdown)
st_button.place(x=200, y=300, width=100, height=50)








st.mainloop()