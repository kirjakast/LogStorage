"""
Programm, mis hoiab baasis logide asukohti
Rakendus, Keskkond
Asukoht

Kasutaja saab:
Vaadata kõiki kirjeid
Otsida kirjeid
Lisada kirjeid
Uuendada kirjeid
Kustutada kirjeid
Sulgeda rakendust
"""
from tkinter import *
import backend

def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
        e5.delete(0,END)
        e5.insert(END,selected_tuple[5])
    except IndexError:
        pass

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(application_text.get(),environment_text.get(),path_text.get(),type_text.get(),note_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(application_text.get(),environment_text.get(),path_text.get(),type_text.get(),note_text.get())
    list1.delete(0,END)
    list1.insert(END,(application_text.get(),environment_text.get(),path_text.get(),type_text.get(),note_text.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],application_text.get(),environment_text.get(),path_text.get(),type_text.get(),note_text.get())

def zero_command():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)

window=Tk()
window.wm_title("LogStorage")

#Lables
l1=Label(window,text="Rakendus")
l1.grid(row=0,column=0,sticky=W)

l2=Label(window,text="Keskkond")
l2.grid(row=1,column=0,sticky=W)

l3=Label(window,text="Asukoht")
l3.grid(row=2,column=0,sticky=W)

l4=Label(window,text="Tüüp")
l4.grid(row=3,column=0,sticky=W)

l5=Label(window,text="Märkmed")
l5.grid(row=4,column=0,sticky=W)

#Entries
#Rakendus
application_text=StringVar()
e1=Entry(window,textvariable=application_text)
e1.grid(row=0,column=1,sticky=W)

#Keskkond
environment_text=StringVar()
e2=Entry(window,textvariable=environment_text)
e2.grid(row=1,column=1,sticky=W)

#Asukoht
path_text=StringVar()
e3=Entry(window,textvariable=path_text,width=100)
e3.grid(row=2,column=1,sticky=W)

#Tüüp
type_text=StringVar()
e4=Entry(window,textvariable=type_text)
e4.grid(row=3,column=1,sticky=W)

#Märkused
note_text=StringVar()
e5=Entry(window,textvariable=note_text,width=100)
e5.grid(row=4,column=1,sticky=W)

#Loome lihtsalt Listboxi
list1=Listbox(window,height=12,width=110)
list1.grid(row=5,column=0,rowspan=8,columnspan=2)

#1. Loome lihtsalt skrollbari
sb1=Scrollbar(window)
sb1.grid(row=5,column=2,rowspan=8)

#2. Seadistame äsja loodud listboxi ja scrollbari, et nad mõistakisd üksteist
list1.configure(yscrollcommand=sb1.set) #Listi y telje küljes on eelnevalt loodud scrollbar
sb1.configure(command=list1.yview)

#Secton 16, Lecture 151
list1.bind('<<ListboxSelect>>',get_selected_row)


#------------------------------NUPUD----------------------------------------------
b1=Button(window,text="Vaata kõiki",width=12,command=view_command)
b1.grid(row=5,column=3,sticky=N)

b2=Button(window,text="Nulli",width=12,command=zero_command)
b2.grid(row=6,column=3,sticky=N)

b3=Button(window,text="Otsi",width=12,command=search_command)
b3.grid(row=7,column=3,sticky=N)

b4=Button(window,text="Lisa",width=12,command=add_command)
b4.grid(row=8,column=3,sticky=N)

b5=Button(window,text="Muuda",width=12, command=update_command)
b5.grid(row=9,column=3,sticky=N)

b6=Button(window,text="Kustuta",width=12,command=delete_command)
b6.grid(row=10,column=3,sticky=N)

b7=Button(window,text="Sulge",width=12,command=window.destroy)
b7.grid(row=11,column=3,sticky=N)



window.mainloop()
