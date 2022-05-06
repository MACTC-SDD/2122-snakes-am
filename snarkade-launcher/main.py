from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import subprocess
import os

p = os.path.dirname(os.path.abspath(__file__))

window=Tk()
window.geometry("500x400")
window.resizable(False,False)
window.title("Snack Arcad")
window['bg']="black"

font1=("Comic Sans MS","16")

def Start():
  def AccessOld():
    def Chosen(number):
      with open(f"{p}/files.txt","r+") as file:
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
              if len(readfiles)>4:
                bodyimglabel5.destroy()
                if len(readfiles)>5:
                  bodyimglabel6.destroy()
                  if len(readfiles)>6:
                    bodyimglabel7.destroy()
                    if len(readfiles)>7:
                      bodyimglabel8.destroy()
                      if len(readfiles)>8:
                        bodyimglabel9.destroy()
                        if len(readfiles)>9:
                          bodyimglabel10.destroy()
        button1.destroy()
        if len(readfiles)>1:
          button2.destroy()
          if len(readfiles)>2:
            button3.destroy()
            if len(readfiles)>3:
              button4.destroy()
              if len(readfiles)>4:
                button5.destroy()
                if len(readfiles)>5:
                  button6.destroy()
                  if len(readfiles)>6:
                    button7.destroy()
                    if len(readfiles)>7:
                      button8.destroy()
                      if len(readfiles)>8:
                        button9.destroy()
                        if len(readfiles)>9:
                          button10.destroy()
        filename=execute[1]
        exec(open(filename).read())
        Start()
    labelthingy.destroy()
    addnew.destroy()
    accessold.destroy()
    with open(f"{p}/files.txt","r+") as file:
      readfile=file.readlines()
      if len(readfile)>0:
        readfile[0]=readfile[0].rstrip()
        image=Image.open(f"{p}/image.png")
        #Start
        bodyimg1=ImageTk.PhotoImage(image)
        bodyimglabel1=Label(window,image=bodyimg1)
        bodyimglabel1.photo=bodyimg1
        bodyimglabel1.place(relx=0,rely=0,anchor=NW)
        splitting=readfile[0].split("=")
        button1=Button(window,text=splitting[0],command=lambda: Chosen(0))
        button1.place(relx=0,rely=.11,anchor=NW)
        if len(readfile)>1:
          #Start
          readfile[1]=readfile[1].rstrip()
          bodyimg2=ImageTk.PhotoImage(image)
          bodyimglabel2=Label(window,image=bodyimg2)
          bodyimglabel2.photo=bodyimg2
          bodyimglabel2.place(relx=.25,rely=0,anchor=N)
          splitting=readfile[1].split("=")
          button2=Button(window,text=splitting[0],command=lambda: Chosen(1))
          button2.place(relx=.25,rely=.11,anchor=N)
          if len(readfile)>2:
            #Start
            readfile[2]=readfile[2].rstrip()
            bodyimg3=ImageTk.PhotoImage(image)
            bodyimglabel3=Label(window,image=bodyimg3)
            bodyimglabel3.photo=bodyimg3
            bodyimglabel3.place(relx=.5,rely=0,anchor=N)
            splitting=readfile[2].split("=")
            button3=Button(window,text=splitting[0],command=lambda: Chosen(2))
            button3.place(relx=.5,rely=.11,anchor=N)
            if len(readfile)>3:
              #Start
              readfile[3]=readfile[3].rstrip()
              bodyimg4=ImageTk.PhotoImage(image)
              bodyimglabel4=Label(window,image=bodyimg4)
              bodyimglabel4.photo=bodyimg4
              bodyimglabel4.place(relx=.75,rely=0,anchor=N)
              splitting=readfile[3].split("=")
              button4=Button(window,text=splitting[0],command=lambda: Chosen(3))
              button4.place(relx=.75,rely=.11,anchor=N)
              if len(readfile)>4:
                #Start
                readfile[4]=readfile[4].rstrip()
                bodyimg5=ImageTk.PhotoImage(image)
                bodyimglabel5=Label(window,image=bodyimg5)
                bodyimglabel5.photo=bodyimg5
                bodyimglabel5.place(relx=1,rely=0,anchor=NE)
                splitting=readfile[4].split("=")
                button5=Button(window,text=splitting[0],command=lambda: Chosen(4))
                button5.place(relx=1,rely=.11,anchor=NE)
                if len(readfile)>5:
                  #Start
                  readfile[5]=readfile[5].rstrip()
                  bodyimg6=ImageTk.PhotoImage(image)
                  bodyimglabel6=Label(window,image=bodyimg6)
                  bodyimglabel6.photo=bodyimg6
                  bodyimglabel6.place(relx=0,rely=.22,anchor=NW)
                  splitting=readfile[5].split("=")
                  button6=Button(window,text=splitting[0],command=lambda: Chosen(5))
                  button6.place(relx=0,rely=.33,anchor=NW)
                  if len(readfile)>6:
                    #Start
                    readfile[6]=readfile[6].rstrip()
                    bodyimg7=ImageTk.PhotoImage(image)
                    bodyimglabel7=Label(window,image=bodyimg7)
                    bodyimglabel7.photo=bodyimg7
                    bodyimglabel7.place(relx=.25,rely=.22,anchor=N)
                    splitting=readfile[6].split("=")
                    button7=Button(window,text=splitting[0],command=lambda: Chosen(6))
                    button7.place(relx=.25,rely=.33,anchor=N)
                    if len(readfile)>7:
                      #Start
                      readfile[7]=readfile[7].rstrip()
                      bodyimg8=ImageTk.PhotoImage(image)
                      bodyimglabel8=Label(window,image=bodyimg8)
                      bodyimglabel8.photo=bodyimg8
                      bodyimglabel8.place(relx=.5,rely=.22,anchor=N)
                      splitting=readfile[7].split("=")
                      button8=Button(window,text=splitting[0],command=lambda: Chosen(7))
                      button8.place(relx=.5,rely=.33,anchor=N)
                      if len(readfile)>8:
                        #Start
                        readfile[8]=readfile[8].rstrip()
                        bodyimg9=ImageTk.PhotoImage(image)
                        bodyimglabel9=Label(window,image=bodyimg9)
                        bodyimglabel9.photo=bodyimg9
                        bodyimglabel9.place(relx=.75,rely=.22,anchor=N)
                        splitting=readfile[8].split("=")
                        button9=Button(window,text=splitting[0],command=lambda: Chosen(8))
                        button9.place(relx=.75,rely=.33,anchor=N)
                        if len(readfile)>9:
                          #Start
                          readfile[9]=readfile[9].rstrip()
                          bodyimg10=ImageTk.PhotoImage(image)
                          bodyimglabel10=Label(window,image=bodyimg10)
                          bodyimglabel10.photo=bodyimg10
                          bodyimglabel10.place(relx=1,rely=.22,anchor=NE)
                          splitting=readfile[9].split("=")
                          button10=Button(window,text=splitting[0],command=lambda: Chosen(9))
                          button10.place(relx=1,rely=.33,anchor=NE)
        window.mainloop()

  def AddNew():
    def Adding():
      checkingtext=authorname.get()
      dirpath=dirname.get()
      if len(checkingtext)>0 and len(dirpath)>0 and ".py" in dirpath.lower():
        checkingtextupper=checkingtext[0].upper()+checkingtext[1:]
        full=checkingtextupper+"="+dirpath
        try:
          with open("files\\"+dirpath,"r+") as file:
            file.close()
          with open(f"{p}/files.txt","r+") as file:
            if full not in file:
              file.write(full+"\n")
        except:
          error['text']="I could not add said file"
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