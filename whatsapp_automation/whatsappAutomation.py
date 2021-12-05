#pip install pywhatkit
import pywhatkit
from tkinter import *
root = Tk()
root.title("Whatsapp Message Automation")
def getvals():
    n_value = nvalue.get()
    msg_value = msgvalue.get()
    hrs_value = hrsvalue.get()
    mins_value = minsvalue.get()
    pywhatkit.sendwhatmsg(n_value, msg_value, hrs_value, mins_value)

#Heading
Label(root, text="Automate message", font="Tahoma",pady=15).grid(row=0, column=3)

#Text for form
n = Label(root,text = "Phone No.")
msg = Label(root, text="Message")
hrs = Label(root, text="Hours(24 hrs format)")
mins = Label(root, text="Minutes")

n.grid(row=1,column =2)
msg.grid(row=3, column=2)
hrs.grid(row=5, column=2)
mins.grid(row=7, column=2)

#storing entries
nvalue = StringVar()
msgvalue = StringVar()
hrsvalue = IntVar()
minsvalue = IntVar()

#entries from form
nentry = Entry(root, textvariable=nvalue)
msgentry = Entry(root, textvariable=msgvalue)
hrsentry = Entry(root, textvariable=hrsvalue)
minsentry = Entry(root, textvariable=minsvalue)

nentry.grid(row =1,column =3)
msgentry.grid(row=3, column=3)
hrsentry.grid(row=5, column=3)
minsentry.grid(row=7, column=3)

Button(text="Submit", command=getvals).grid(row=15, column=3)

root.geometry("644x434")

root.mainloop()