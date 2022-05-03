from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import subprocess

window=Tk()
window.geometry("500x400")
window.title("Snack Arcad")
window['bg']="black"

font1=("Comic Sans MS","16")

def Start():
  def AccessOld():
    def Chosen(number):
      with open("files.txt","r+") as file:
        readfiles=file.readlines() 
        readfiles[number]=readfiles[number].rstrip()
        execute=readfiles[number].split("=")
        bodyimglabel1.destroy()
        if len(readfiles)>1:
          bodyimglabel2.destroy()
          if len(readfiles)>2:
            bodyimglabel3.destroy()
            if len(readfiles)>3:
              bodyimglabel4.destroy()
        button1.destroy()
        if len(readfiles)>1:
          button2.destroy()
          if len(readfiles)>2:
            button3.destroy()
            if len(readfiles)>3:
              button4.destroy()
        filename=execute[1]
        exec(open(filename).read())
    labelthingy.destroy()
    addnew.destroy()
    accessold.destroy()
    with open("files.txt","r+") as file:
      readfile=file.readlines()
      if len(readfile)>0:
        readfile[0]=readfile[0].rstrip()
        image=Image.open("image.png")
        #Start
        bodyimg1=ImageTk.PhotoImage(image)
        bodyimglabel1=Label(window,image=bodyimg1)
        bodyimglabel1.photo=bodyimg1
        bodyimglabel1.grid(column=0,row=0)
        splitting=readfile[0].split("=")
        button1=Button(window,text=splitting[1],command=lambda: Chosen(0))
        button1.grid(column=0,row=1)
        if len(readfile)>1:
          #Start
          readfile[1]=readfile[1].rstrip()
          bodyimg2=ImageTk.PhotoImage(image)
          bodyimglabel2=Label(window,image=bodyimg2)
          bodyimglabel2.photo=bodyimg2
          bodyimglabel2.grid(column=1,row=0)
          splitting=readfile[1].split("=")
          button2=Button(window,text=splitting[1],command=lambda: Chosen(1))
          button2.grid(column=1,row=1)
          if len(readfile)>2:
            #Start
            readfile[2]=readfile[2].rstrip()
            bodyimg3=ImageTk.PhotoImage(image)
            bodyimglabel3=Label(window,image=bodyimg3)
            bodyimglabel3.photo=bodyimg3
            bodyimglabel3.grid(column=2,row=0)
            splitting=readfile[2].split("=")
            button3=Button(window,text=splitting[1],command=lambda: Chosen(2))
            button3.grid(column=2,row=1)
            if len(readfile)>3:
              #Start
              readfile[3]=readfile[3].rstrip()
              bodyimg4=ImageTk.PhotoImage(image)
              bodyimglabel4=Label(window,image=bodyimg4)
              bodyimglabel4.photo=bodyimg4
              bodyimglabel4.grid(column=3,row=0)
              splitting=readfile[3].split("=")
              button4=Button(window,text=splitting[1],command=lambda: Chosen(3))
              button4.grid(column=3,row=1)
        window.mainloop()

  def AddNew():
    def Adding():
      checkingtext=authorname.get()
      dirpath=dirname.get()
      if len(checkingtext)>0 and len(dirpath)>0:
        checkingtextupper=checkingtext[0].upper()+checkingtext[1:]
        full=checkingtextupper+"="+dirpath
        try:
          with open("files\\"+dirpath,"r+") as file:
            file.close()
          with open("files.txt","r+") as file:
            if full not in file:
              file.write(full+"\n")
        except:
          error['text']="I could not file said file"
          pass
    def Back():
      author.destroy()
      authorname.destroy()
      dirtext.destroy()
      dirname.destroy()
      addbutton.destroy()
      backbutton.destroy()
      error.destroy()
      Start()
    labelthingy.destroy()
    addnew.destroy()
    accessold.destroy()
    author=Label(window,text="Author",bg="grey",fg="white")
    author.place(relx=.25,rely=0,anchor=N)
    authorname=Entry(window,width=12)
    authorname.place(relx=.25,rely=.1,anchor=N)
    #Actual Name
    #Actual Directory
    dirtext=Label(window,text="Full Directory Path",bg="grey",fg="white")
    dirtext.place(relx=.75,rely=0,anchor=N)
    dirname=Entry(window,width=12)
    dirname.place(relx=.75,rely=.1,anchor=N)
    addbutton=Button(window,text="Add", fg="blue",bg="grey",command=lambda: Adding())
    addbutton.place(relx=.5,rely=.05,anchor=N)
    backbutton=Button(window,text="Back", fg="blue",bg="grey",command=lambda: Back())
    backbutton.place(relx=.5,rely=.15,anchor=N)
    error=Label(window,text="Files Openable",fg="white",bg="black")
    error.place(relx=.5,rely=.3,anchor=N)

  labelthingy=Label(window,text="Snack Arcad",fg="white",bg="grey",font=font1)

  addnew=Button(window,text="Add New",fg="blue",bg="grey",command=lambda: AddNew())
  addnew.place(relx=.5,rely=.2,anchor=N)

  accessold=Button(window,text="Play Added",fg="blue",bg="grey",command=lambda: AccessOld())
  accessold.place(relx=.5,rely=.3,anchor=N)

  labelthingy.place(relx=.5,rely=.05,anchor=N)

  window.mainloop()
Start()
