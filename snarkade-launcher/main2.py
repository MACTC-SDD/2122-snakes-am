import os
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from PIL import Image,ImageTk
import subprocess

p = os.path.dirname(os.path.abspath(__file__))
BUTTONS_PER_ROW = 4
GAME_PATH = '~/Documents/Git/2122-snakes-am'
PYTHON3 = '/usr/bin/python3'

COVERX = 40
COVERY = 40

try:
  from env import env
  GAME_PATH = env['GAME_PATH']
  PYTHON3 = env['PYTHON3']
except ImportError:
  pass

print (f'{GAME_PATH}, {PYTHON3}')
exit()

window=Tk()
window.geometry("550x400")
window.resizable(False,False)
window.title("Snack Arcad")
window['bg']="black"

font1=("Comic Sans MS","16")

images = {'None': PhotoImage(file=f'{p}/image.png')}

play_buttons = []
main_widgets = []
add_widgets = []

# Display the main menu
def main_menu():
  global main_widgets
  clear_widgets(play_buttons + add_widgets )
  labelthingy=Label(window,text="Snack Arcad",fg="white",bg="grey",font=font1)

  addnew=Button(window,text="Add New",fg="blue",bg="grey",command=add_menu)
  addnew.place(relx=.5,rely=.2,anchor=N)

  accessold=Button(window,text="Play Added",fg="blue",bg="grey",command=launch_menu)
  accessold.place(relx=.5,rely=.3,anchor=N)

  labelthingy.place(relx=.5,rely=.05,anchor=N)
  main_widgets.extend([labelthingy, addnew, accessold])

# Display all play buttons
def launch_menu():
  clear_widgets(main_widgets + add_widgets)
  read_config()
  place_buttons(play_buttons)

# Display add item 
def add_menu():
  global add_widgets
  clear_widgets(main_widgets + play_buttons)

  author=Label(window,text="Author",bg="grey",fg="white")
  author.place(relx=.25,rely=0,anchor=N)
  authorname=Entry(window,width=12)
  authorname.place(relx=.25,rely=.1,anchor=N)
  dirtext=Label(window,text="Full Directory Path",bg="grey",fg="white")
  dirtext.place(relx=.75,rely=0,anchor=N)
  dirname=Entry(window,width=12)
  dirname.place(relx=.75,rely=.1,anchor=N)
  error=Label(window,text="",fg="white",bg="black")
  addbutton=Button(window,text="Add", fg="blue",bg="grey",command=lambda title_w=authorname,
    file_path_w=dirname, error=error: add_entry(title_w,file_path_w,error))
  addbutton.place(relx=.5,rely=.05,anchor=N)
  backbutton=Button(window,text="Back", fg="blue",bg="grey",command=main_menu)
  backbutton.place(relx=.5,rely=.15,anchor=N)
  error.place(relx=.5,rely=.3,anchor=N)

  add_widgets.extend([author, authorname, dirtext, dirname])
  add_widgets.extend([addbutton, backbutton, error])

# Add item to config file
def add_entry(title_w, file_path_w, error, image_path = 'cover.png'):
  # We need to pass in the widget objects so we can query for value
  title = title_w.get()
  file_path = file_path_w.get()

  if len(title)>0 and len(file_path)>0 and ".py" in file_path.lower():
    title = title[0].upper() + title[1:]
    entry = f'{title}:{file_path}:{image_path}'

    # If no leading / consider path relative to running path
    file_path = localize_path(file_path)

    if not os.path.exists(file_path):
      error['text'] = 'File not found.'
    else:
      try:
        with open(f"{p}/files.txt","r+") as file:
          if entry not in file:
            file.write(entry+"\n")
        error['text'] = "Entry saved."
      except:
        error['text']="I could not add said file."
      
# Destroy all specified widgets
def clear_widgets(widgets_to_remove):
  for w in widgets_to_remove:
    w.destroy()

# Run this when play button is clicked
def play_clicked(idx=0):
  button = play_buttons[idx]
  file_path = localize_path(button.file_path)
  # Use .run if you want it to block until subprocess completes
  subprocess.Popen([PYTHON3, file_path])

# Read all items from config file and create play buttons
def read_config():
  global play_buttons
  global images

  with open(f"{p}/files.txt","r+") as file:
    for line in file.readlines():
      line = line.rstrip()
      image_path = 'cover.png'
      img = images['None']

      kvp = line.split(':')
      title,path = kvp[0],kvp[1]
      # Image (if specified and exists) will come from individual game path
      # It will default to cover.png but could be edited in config file directly
      # Images will be resized to COVERX/COVERY 
      if len(kvp) > 2:
        image_path = kvp[2]
        image_path = f'{os.path.dirname(localize_path(path))}/{image_path}'
        if os.path.exists(image_path):
          i = Image.open(image_path)
          i = i.resize((COVERX,COVERY), Image.ANTIALIAS)
          images[line] = ImageTk.PhotoImage(i)
          img = images[line]  
 
      # TODO: Limit title to 20 chars? Or word wrap?

      img_button = Button(
        window,
        image=img,
        text=title,
        compound=TOP,
        width=100,
        command = lambda idx = len(play_buttons): play_clicked(idx)
      )
      img_button.file_path = path
      play_buttons.append(img_button)

# Place play buttons
def place_buttons(buttons):
  x,y = 0,0
  for button in buttons:
    button.grid(row=y,column=x,ipadx=15,ipady=15)
    x += 1
    if x > BUTTONS_PER_ROW-1:
      x = 0
      y += 1
    
# If we don't start with root path, add running path
def localize_path(file_path):
  if file_path[0] != '/':
    # Use GAME_PATH if specified
    if GAME_PATH == '':
      file_path = f'{p}/{file_path}'
    else:
      file_path = f'{GAME_PATH}/{file_path}'

  return file_path

# Start with the main menu and go from there
main_menu()

window.mainloop()

