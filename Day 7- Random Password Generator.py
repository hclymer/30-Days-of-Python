import secrets
import string
from msilib.schema import CheckBox
import random
from tkinter import *
import tkinter



#creating a window 

window = Tk()

#title of window
window.title("random password generator")

#size of window
window.geometry("600x600")

#label
Label(window, font=('bold',8), text="Generate Password").pack()

#converting the length into an integer
length1 = tkinter.IntVar()
length2 = tkinter.IntVar()
length3 = tkinter.IntVar()
length4 = tkinter.IntVar()
length5 = tkinter.IntVar()

#function to generate random password
def passwordGeneration(n):
    
    # letters= string.ascii_letters
    # digits = string.digits
    # special_chars = string.punctuation

    # #generating random password
    # alphabet = letters + digits + special_chars
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@_'

    
    password = ''.join(random.sample(characters, n))
    l = Label(window, text= password, font=('bold', 15)) #dispaly password
    l.place(x=225, y=65)
    
def getLength():
    if length1.get() == 4:
        passwordGeneration(4)
    elif length2.get() == 6:
        passwordGeneration(6)
    elif length3.get() == 8:
        passwordGeneration(8)
    elif length4.get() == 10:
        passwordGeneration(10)
    else:
        passwordGeneration(12)
        
#creating buttons
Button(window, text="Generate Password", font=("normal",10), bg='green', command=getLength).place(x=230,y=100)

Checkbutton(text= '4 characters', onvalue= 4, offvalue= 0, variable= length1).place(x=250,y=150)
Checkbutton(text= '6 characters', onvalue= 6, offvalue= 0, variable= length2).place(x=250,y=170)
Checkbutton(text= '8 characters', onvalue= 8, offvalue= 0, variable= length3).place(x=250,y=190)
Checkbutton(text= '10 characters', onvalue= 10, offvalue= 0, variable= length4).place(x=250,y=210)
Checkbutton(text= '12 characters', onvalue= 12, offvalue= 0, variable= length5).place(x=250,y=230)

window.mainloop()

     

