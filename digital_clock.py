import tkinter as tk      #tkinter used in python for graphical interface (GUI)
from time import strftime
#time module used to time module function
root = tk.Tk()    #displayed the element used root
root.title("Digital Clock")

def time():  #used function for update the time and date
    string= strftime('%H:%M:%S %p \n %D')
    label.config(text=string)    #label of config method to convert the text to string 
    label.after(1000,time)

label=tk.Label(root,font=('calibri',50,'bold'),background='black',foreground='white')
label.pack(anchor='center')

time()
root.mainloop()